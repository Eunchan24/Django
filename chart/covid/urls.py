from django.urls import path
from . import views
app_name = 'graph'
urlpatterns = [
    path('covid19/', views.covid_chart, name = 'covid-chart'),
]