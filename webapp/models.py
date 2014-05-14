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
    def get_last(self):
        return modbusDevice.get_data()
