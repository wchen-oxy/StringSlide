from django.shortcuts import render
from django.http import HttpResponse
from .models import Guitar

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the entries")

def home(request):
    
    return render(request, 'home.html')