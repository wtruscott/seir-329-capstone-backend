from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal

def index(request):
    Animals = Animal.objects
    print(Animals.all()[0].name)
    return HttpResponse('Hello World')

def other(request):
    Animals.create(name="Human", legs=2)
    return render(request, 'animals/other.html', {"animal":Animals.all() })
# Create your views here.
