from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def project(request):
    return HttpResponse("Here are our products")

def projects(request,pk):
    return HttpResponse("Single our products"+' ' + str(pk))

