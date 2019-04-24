from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

import random
from .models import Guitar

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the entries")

def home(request):
    guitar_id = random.randint(0, 999)
    chosen = get_object_or_404(Guitar, pk=guitar_id)
    picked = Guitar.objects.get(guitar_id=1)
    print(chosen)
    print(picked)
    
    return render(request, 'home.html', {'place': picked.guitar_name})