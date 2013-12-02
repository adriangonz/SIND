from django.shortcuts import render


def index(request):
    template_value = {
        'title': 'Titulo',
        'message': 'Some message'
    }
    return render(request, 'webapp/index.html', template_value)


def chart_test(request):
    return render(request, 'webapp/chart.html', {})
