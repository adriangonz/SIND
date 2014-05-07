#!/usr/local/bin/python
import random
import sys
import sched, time, csv, os
import shutil
import threading
import os.path 
from pymodbus.client.sync import ModbusSerialClient
from datetime import datetime


class ModbusClient(object):

    """Cliente ModBus sencillo"""

    def __init__(self, device_id, port='/dev/ttyUSB0'):
        super(ModbusClient, self).__init__()
        self.device_id = device_id
        self.client = ModbusSerialClient(method='rtu', port=port,
                                         baudrate=9600, bytesize=8,
                                         parity='N', stopbits=2,
                                         timeout=0.05, writeTimeout=1.5)

    def write_registers(self, address, data):
        """ Escribe una serie de registros en el dispositivo """
        self.client.write_registers(address, data, unit=self.device_id)


    def read_registers(self, address, count=1):
        result = self.client.read_holding_registers(
            address, count, unit=self.device_id)
        if count == 1:
            registers = result.getRegister(0)
        else:
            registers = []
            for reg_index in range(0, count):
                registers.append(result.getRegister(reg_index))
        return registers
 
    def to_hex(self,integer):
        return "0x%0.4X" % integer
    
    def split_hex(self, integer):
        return integer / 256, integer % 256
    
    def get_device_datetime(self,client):
	req = client.read_holding_registers(253, 3, unit=25)
	secmin = self.to_hex(req.getRegister(0))
	hourday = self.to_hex(req.getRegister(1))
	monthyear = self.to_hex(req.getRegister(2))
	month, year = self.split_hex(monthyear)
	hour, day = self.split_hex(hourday)
	sec, min = self.split_hex(secmin)
	return datetime(int(year) + 2000, int(month), int(day), int(hour), int(min), int(sec))
    
    def get_row(self):
	# Get V
	req = self.client.read_holding_registers(2, 1, unit=25)
	V = req.getRegister(0) / 100.0
	# Get I
	req = self.client.read_holding_registers(7, 2, unit=25)
	I = int(self.to_hex(req.getRegister(0)) + (self.to_hex(req.getRegister(1))[2:]), 16) / 1000.0
	# Get PAct
	req = self.client.read_holding_registers(21, 2, unit=25)
	PAct = int(self.to_hex(req.getRegister(1)) + (self.to_hex(req.getRegister(0))[2:]), 16) / 100.0
	# Get PReact
	req = self.client.read_holding_registers(29, 2, unit=25)
	PReact = int(self.to_hex(req.getRegister(1)) + (self.to_hex(req.getRegister(0))[2:]), 16) / 100.0
	# Get FactorPotencia
	req = self.client.read_holding_registers(10, 1, unit=25)
	FactorPotencia = req.getRegister(0) / 1000.0
	# Get Frec
	req = self.client.read_holding_registers(9, 1, unit=25)
	Frec = req.getRegister(0) / 100.0
	# Get PAparente
	req = self.client.read_holding_registers(11, 2, unit=25)
	PAparente = int(self.to_hex(req.getRegister(1)) + (self.to_hex(req.getRegister(0))[2:]), 16) / 100.0
	# Return row
	return [
		self.get_device_datetime(self.client).isoformat(),
		V,
		I,
		PAct,
		PReact,
		FactorPotencia,
		Frec,
		PAparente
	]
    
    def cycle_csv(self,s,num):
        filename = 'practica_prueba.txt'
	#if os.path.exists(filename):
		#header_exists = True
	#else:
		#header_exists = False
	with open(filename, 'a+') as csvfile:
		writer = csv.writer(csvfile)
		#if not header_exists:
                #row = [
                #                'fecha '+str(num),
                #                'V '+str(num),
                #                'I '+str(num),
                #                'PAct '+str(num),
                #                'PReact '+str(num),
                #                'FactorPotencia '+str(num),
                #                'Frec '+str(num),
                #                'PAparente '+str(num)
                #]
                #writer.writerow(row)
		row = self.get_row()
		writer.writerow(row)
		print >> sys.stderr,row
                csvfile.close()
	s.enter(1, 1, self.cycle_csv, (s,num+1,))
    
    def store_registers(self):
        s = sched.scheduler(time.time, time.sleep)
	s.enter(1, 1, self.cycle_csv, (s,0,))
	s.run()
        
    def get_data(self,s):
        shutil.copyfile('practica_prueba.txt', 'auxiliar.txt')
        filename = 'auxiliar.txt'
	"""
        with open(filename, 'a+') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print row
            csvfile.close()
        """
        s.enter(1, 1, self.get_data, (s,))
    
    def getting_data(self):
        while not os.path.exists('practica_prueba.txt'):
            pass
        s = sched.scheduler(time.time, time.sleep)
	s.enter(1, 1, self.get_data, (s,))
	s.run() 
        

class ModbusDeviceInterface(object):

    """ Interfaz generica con el dispositivo ModBus """

    def get_datetime(self):
        pass

    def set_datetime(self, new_datetime):
        pass

    def get_data(self):
        pass


class ModbusMockDevice(ModbusDeviceInterface):

    """ Dispositivo ModBus "dummy" """
    def __init__(self):

        self.modbus_client = ModbusClient(device_id=25)
        t = threading.Thread(target=self.modbus_client.store_registers)
        t.start()
        t2 = threading.Thread(target=self.modbus_client.getting_data)
        t2.start()
        self.datetime = datetime.now()

    def get_datetime(self):
        return self.datetime

    def set_datetime(self, new_datetime):
        self.datetime = new_datetime
        return self.datetime

    def get_data(self):
        
        return {
            'Fecha': self.get_datetime(),
            'V': random.uniform(220.0, 240.0),
            'I': random.uniform(1500.0, 1800.0),
            'PAct': random.uniform(180000.0, 200000.0),
            'PReact': random.uniform(0.0, 1.0),
            'FactorPotencia': random.uniform(0.1, 1.0),
            'Frec': random.uniform(45.0, 50.0),
            'PAparente': random.uniform(300000.0, 320000.0)
        }


class ModbusDevice(ModbusDeviceInterface):

    """ Dispositivo real compatible con ModBus """

    def __init__(self, device_id):
        super(ModbusDevice, self).__init__()
        self.modbus_client = ModbusClient(device_id=device_id)

    def _to_hex(self, integer):
        """ Pasa un entero a hexadecimal """
        return ("0x%0.4X") % integer

    def _to_int(self, hexadec):
        return int(hexadec[2:], 16)

    def _split_hex(self, integer):
        return integer / 256, integer % 256

    def _join_hex(self, a, b):
        return a * 256 + b

    def _join_high_low(self, hex_list):
        return hex_list[0] * 65536 + hex_list[1]

    def _read_high_low(self, address):
        return self._join_high_low(self.modbus_client.read_registers(address, 2))

    def get_datetime(self):
        date_registers = self.modbus_client.read_registers(253, 3)
        seconds, minutes = self._split_hex(date_registers[0])
        hour, day = self._split_hex(date_registers[1])
        month, year = self._split_hex(date_registers[2])
        return datetime(year + 2000, month, day, hour, minutes, seconds)

    def set_datetime(self, new_datetime):
        secmin = self._join_hex(new_datetime.second, new_datetime.minute)
        hourday = self._join_hex(new_datetime.hour, new_datetime.day)
        monthyear = self._join_hex(new_datetime.month, new_datetime.year % 2000)
        self.modbus_client.write_registers(253, [secmin, hourday, monthyear])
        return True

    def get_data(self):
        return {
            'V': self.modbus_client.read_registers(2) / 100.0,
            'I': self._read_high_low(7) / 1000.0,
            'PAct': self._read_high_low(21) / 100.0,
            'PReact': self._read_high_low(29) / 100.0,
            'FactorPotencia': self.modbus_client.read_registers(10) / 1000.0,
            'Frec': self.modbus_client.read_registers(9) / 100.0,
            'PAparente': self._read_high_low(11) / 100.0
        }
