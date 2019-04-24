from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

import random
from .models import Guitar

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the entries")

def home(request):

    guitar = Guitar.objects.get(guitar_id=1)
    guitar2 = Guitar.objects.get(guitar_id=2)
    guitar3 = Guitar.objects.get(guitar_id=3)


    
    return render(request, 'home.html', {'guitar_id': guitar.guitar_id,
                                         'guitar_model':guitar.guitar_model,
                                         'guitar_name': guitar.guitar_name,

                                         'guitar_id2': guitar2.guitar_id,
                                         'guitar_model2': guitar2.guitar_model,
                                         'guitar_name2': guitar2.guitar_name,

                                         'guitar_id3': guitar3.guitar_id,
                                         'guitar_model3': guitar3.guitar_model,
                                         'guitar_name3': guitar3.guitar_name,

                                         })