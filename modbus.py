#!/usr/bin/python

from pymodbus.client.sync import ModbusSerialClient


class ModbusClient(object):

    """Cliente ModBus sencillo"""

    def __init__(self, device, port='/dev/ttyUSB0'):
        super(ModbusClient, self).__init__()
        self.device = device
        self.client = ModbusSerialClient(method='rtu', port=port,
                                         baudrate=9600, bytesize=8,
                                         parity='N', stopbits=2,
                                         timeout=0.05, writeTimeout=1.5)

    def write_registers(self, address, data):
        """ Escribe una serie de registros en el dispositivo """
        self.client.write_registers(address, data, unit=self.unit)

    def read_registers(self, address, count=1):
        register_list = []
        result = self.client.read_holding_registers(
            address, count, unit=self.unit)
        for reg_index in range(0, count):
            register_list.append(result.getRegister(reg_index))
        return register_list


class ModbusDevice(object):

    """ Dispositivo compatible con modbus """

    def __init__(self, device):
        super(ModbusDevice, self).__init__()
        self.modbusclient = ModbusClient(device=device)

    def _to_hex(self, integer):
        """ Pasa un entero a hexadecimal """
        return ("0x%0.4X") % integer

    def _to_int(self, hexadec):
        return int(hexadec[2:], 16)

    def _split_hex(self, integer):
        return integer / 256, integer % 256

if __name__ == '__main__':
    prueba = ModbusDevice(25)
    assert prueba._to_int('0x0B0D') == 2829
    assert prueba._to_hex(2829) == '0x0B0D'
    print prueba._split_hex(2829)
