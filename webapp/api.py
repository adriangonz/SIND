# REST API Controllers
import json
import dateutil.parser
from django.http import HttpResponse
from django.conf.urls import patterns, url
from django.views.generic import View
from django.core import serializers
from modbus import ModbusMockDevice
from models import ModbusData

modbusDevice = ModbusMockDevice()


class DateController(View):
    """ Simple controller for managing date """

    def _json(self, datetime):
        return json.dumps({
            'date': datetime.isoformat()
        })

    def get(self, request):
        return HttpResponse(self._json(modbusDevice.get_datetime()))

    def post(self, request):
        date_isoformat = request.POST.get('date', None)
        if date_isoformat is None:
            return HttpResponse(status=400)
        date = dateutil.parser.parse(date_isoformat)
        if not modbusDevice.set_datetime(date):
            return HttpResponse(status=500)
        return HttpResponse(self._json(date), status=200)


class InfoController(View):
    """ Simple controller for managing date """

    def get(self, request):
        return HttpResponse(
            serializers.serialize('json', ModbusData.get_last()))


urls = patterns(
    '',
    url(r'^date', DateController.as_view()),
    url(r'^info', InfoController.as_view())
)
