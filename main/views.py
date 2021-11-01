from time import sleep
from django.shortcuts import render
from django.http import HttpResponse
from main.tasks import test_func

# Create your views here.
def home(request):
    test_func.delay()
    # for i in range(20):
    #     print(i)
    #     sleep(1)
    return HttpResponse('Done')