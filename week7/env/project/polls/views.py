from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse ("I have a dog name spot. He is a large dog! Spot like to play." )