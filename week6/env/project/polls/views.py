from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return HttpResponse("<p>I have a large backyard and a small garden.Roses are red!I am happy to have my own home!</p><p>The sun is shinning,I have a beautiful view of the park.Its is located in Frisco Texas!</p>")