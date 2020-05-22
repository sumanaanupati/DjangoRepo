from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse
from . import utils

def hello(request):
    return render(request,'welcome.html',context=utils.get_data_from_url())


def trend(request,country):
    return render(request,'trend.html',context={'country':utils.get_country_data(country)})