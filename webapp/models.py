from django.db import models

class ModbusData(models.Model):
    Fecha = models.DateField()
    V = models.FloatField()
    I = models.FloatField()
    PAct = models.FloatField()
    PReact = models.FloatField()
    FactorPotencia = models.FloatField()
    Frec = models.FloatField()
    PAparente = models.FloatField()