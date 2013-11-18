from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template_value = {
        'title': 'Titulo',
        'message': 'Some message'
    }
    return render(request, 'webapp/index.html', template_value)
