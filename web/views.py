from django.shortcuts import render
import os
import pandas as pd
# Create your views here.
from web.processing import fun
def index(request):
    return render(request , 'web/index.html')


def result(request):
    if request.method == 'POST':
        text = request.POST['csvfile']
        val = "web/dataset/" + text
        l = fun(val)
        print(l)
        return render(request , 'web/index.html' , {'text':text , 'data':l})



    return render(request , 'web/index.html')