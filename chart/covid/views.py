from django.shortcuts import render

# Create your views here.

from covid.models import Covid19
from django.http import JsonResponse
from django.db.models import Sum
def covid_chart(request):
    labels = []
    data = []
    data2 = []
    data3 = []
    #  'deathcnt', 'decidecnt', 'createdt',  'accexamcompcnt'
    queryset = Covid19.objects.all()
    for covid in queryset[1:]:
        labels.append(str(covid.createdt)[:10])
        data.append(covid.decidecnt)
        data2.append(covid.deathcnt)
        data3.append(covid.accexamcompcnt)
    return render(request, 'covid_chart.html', {
        'labels': labels,
        'data': data,
        'data2' : data2,
        'data3' : data3,
    })