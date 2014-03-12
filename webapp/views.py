from django.shortcuts import render
from django.core import serializers
from modbus import ModbusMockDevice
from models import ModbusData


modbusDevice = ModbusMockDevice()


def index(request):
    template_value = {
        'data': serializers.serialize('json', ModbusData.get_last()),
        'date': modbusDevice.get_datetime().isoformat()
    }
    return render(request, 'webapp/index.html', template_value)


def index_old(request):
    template_value = {
        'data': serializers.serialize('json', ModbusData.get_last()),
        'date': modbusDevice.get_datetime().isoformat()
    }
    return render(request, 'webapp/index_old.html', template_value)


def chart_test(request):
    return render(request, 'webapp/chart.html', {})
