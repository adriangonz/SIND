from django.db import models
from modbus import ModbusMockDevice

modbusDevice = ModbusMockDevice()


class ModbusData(models.Model):

    Vmedio = models.FloatField()
    Imedia = models.FloatField()
    P = models.FloatField()
    ConsumoInst = models.FloatField()
    ConsumoDiario = models.FloatField()

    @classmethod
    def set_data(self):
        data_dict = modbusDevice.get_data()
        new_data = ModbusData()
        new_data.Vmedio = data_dict['Vmedio']
        new_data.Imedia = data_dict['Imedia']
        new_data.P = data_dict['P']
        new_data.ConsumoInst = data_dict['ConsumoInst']
        new_data.ConsumoDiario = data_dict['ConsumoDiario']
        new_data.save()

    @classmethod
    def get_last(self):
        return ModbusData.objects.all()
