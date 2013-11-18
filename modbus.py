#!/usr/local/bin/python

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
        register_list = []
        result = self.client.read_holding_registers(
            address, count, unit=self.device_id)
        for reg_index in range(0, count):
            register_list.append(result.getRegister(reg_index))
        return register_list


class ModbusDevice(object):

    """ Dispositivo compatible con modbus """

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

if __name__ == '__main__':
    prueba = ModbusDevice(25)
    prueba.set_datetime(datetime.now())
    print prueba.get_datetime()
