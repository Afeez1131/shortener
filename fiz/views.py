from django.shortcuts import render, HttpResponse
from .models import fizzURL


def home(request):

    return HttpResponse('<h1>Welcome Home</h1>')