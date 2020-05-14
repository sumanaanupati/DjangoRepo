from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse

def hello(request):
    user_data = {
        'users':[{'name':'sumana','place':'Mancherial','search':'ShreyaGoshal'},
        {'name':'Sumanth','place':'Khammam','search':'LinkinPark'},
        {'name':'Lavanya','place':'Vizag','search':'Crafting'},
        {'name':'Moulika','place':'Kurnool','search':'Yoga'},
        {'name':'Murali','place':'cuddapah','search':'Games'}]
    }
    return render(request,'welcome.html',context=user_data)
