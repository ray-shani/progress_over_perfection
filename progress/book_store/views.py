from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request): # <--- This function definition
    """
    A simple view that returns a welcome message for the book store.
    """
    return HttpResponse("Welcome to my book store.")