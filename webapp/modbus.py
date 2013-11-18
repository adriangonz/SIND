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
        result = self.client.read_holding_registers(
            address, count, unit=self.device_id)
        if count == 1:
            registers = result.getRegister(0)
        else:
            registers = []
            for reg_index in range(0, count):
                registers.append(result.getRegister(reg_index))
        return registers


class ModbusDevice(object):

    """ Dispositivo compatible con ModBus """

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

if __name__ == '__main__':
    prueba = ModbusDevice(25)
    print prueba.get_data()