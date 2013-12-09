from django.db import models
from modbus import ModbusMockDevice

modbusDevice = ModbusMockDevice()


class ModbusData(models.Model):

    Fecha = models.DateTimeField()
    V = models.FloatField()
    I = models.FloatField()
    PAct = models.FloatField()
    PReact = models.FloatField()
    FactorPotencia = models.FloatField()
    Frec = models.FloatField()
    PAparente = models.FloatField()

    @classmethod
    def set_data(self):
        data_dict = modbusDevice.get_data()
        new_data = ModbusData()
        new_data.Fecha = data_dict['Fecha']
        new_data.V = data_dict['V']
        new_data.I = data_dict['I']
        new_data.PAct = data_dict['PAct']
        new_data.PReact = data_dict['PReact']
        new_data.FactorPotencia = data_dict['FactorPotencia']
        new_data.Frec = data_dict['Frec']
        new_data.PAparente = data_dict['PAparente']
        new_data.save()

    @classmethod
    def get_last(self):
        return ModbusData.objects.all()
