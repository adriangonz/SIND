from django.db import models

class ModbusData(models.Model):
    Fecha = models.DateField()
    V = models.FloatField
    I = models.CharField(max_length=50)
    PAct = models.CharField(max_length=60)
    PReact = models.CharField(max_length=30)
    FactorPotencia = models.CharField(max_length=50)
    Frec = models.CharField(max_length=50)
    PAparente = models.CharField(max_length=50)