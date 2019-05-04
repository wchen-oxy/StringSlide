from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db import connection

import random
from .models import Guitar, Story, Photos, Specs, Appearances

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the entries")

def home(request):
    num = random.randint(1,999)
    num2 = random.randint(1,999)

    guitar = Guitar.objects.get(guitar_id=num)
    g_photo = Photos.objects.get(guitar_id=num)
    g_story = Story.objects.get(guitar_id=num)
    guitar2 = Guitar.objects.get(guitar_id=num2)
    g_photo2 = Photos.objects.get(guitar_id=num2)
    g_story2 = Story.objects.get(guitar_id=num2)
    guitar3 = Guitar.objects.get(guitar_id=1001)
    g_photo3 = Photos.objects.get(guitar_id=10)
    g_story3 = Story.objects.get(guitar_id=10)

    text_1 = g_story.story_text;
    text_1 = (text_1[:100] + '...') if len(text_1) > 103 else text_1
    text_2 = g_story2.story_text;
    text_2 = (text_2[:100] + '...') if len(text_2) > 103 else text_2
    text_3 = g_story3.story_text;
    text_3 = (text_3[:100] + '...') if len(text_3) > 103 else text_3


    return render(request, 'home.html', {'guitar_id': guitar.guitar_id,
                                         'guitar_model': guitar.guitar_model,
                                         'guitar_name': guitar.guitar_name,
                                         'guitar_image' : g_photo.photo_path,
                                         'guitar_summary' : text_1,

                                         'guitar_id2': guitar2.guitar_id,
                                         'guitar_model2': guitar2.guitar_model,
                                         'guitar_name2': guitar2.guitar_name,
                                         'guitar_image2' : g_photo2.photo_path,
                                         'guitar_summary2' : text_2,

                                         'guitar_id3': guitar3.guitar_id,
                                         'guitar_model3': guitar3.guitar_model,
                                         'guitar_name3': guitar3.guitar_name,
                                         'guitar_image3' : g_photo3.photo_path,
                                         'guitar_summary3' : text_3,

                                         })

# def new(request):


def entry_page(request, guitar_id):

    repaired = ""
    prev = ""
    next = ""
    guitar = Guitar.objects.get(guitar_id=guitar_id)
    story = Story.objects.get(guitar_id=guitar_id)
    photo = Photos.objects.get(guitar_id=guitar_id)
    spec = Specs.objects.get(guitar_id=guitar_id)
    try:
        appear_tour = Appearances.objects.get(guitar_id=guitar_id).tour_name
    except:
        appear_tour = "None"

    try:
        appear_album = Appearances.objects.get(guitar_id=guitar_id).album_name
    except:
        appear_album = "None"


    if int(guitar.guitar_id) != 1:
        prev = "/entries/" + str(int(guitar.guitar_id) - 1)
        next = "/entries/" + str(int(guitar.guitar_id) + 1)
    else:
        prev = "/entries/" + str(1)
        next = "/entries/" + str(int(guitar.guitar_id) + 1)

    if spec.repairs == 1:
        repaired = "Yes"
    else:
        repaired = "None"



    return render(request, 'entries/entry.html', {'guitar_id': guitar.guitar_id,
                                                  'guitar_man': guitar.manufacturer_name,
                                         'guitar_model':guitar.guitar_model,
                                         'guitar_name': guitar.guitar_name,
                                          'story':story.story_text,
                                                  'photo':photo.photo_path,
                                                  'production_year':spec.production_year,
                                                  'finish':spec.finish,
                                                  'weight':spec.weight,
                                                  'body_wood':spec.body_wood,
                                                  'neck_wood':spec.neck_wood,
                                                  'fretboard_wood':spec.fretboard_wood,
                                                  'cap_wood':spec.cap_wood,
                                                  'neck_pick':spec.neck_pickup,
                                                  'middle_pickup':spec.middle_pickup,
                                                  'bridge_pickup':spec.bridge_pickup,
                                                  'repairs':repaired,
                                                  'tour': appear_tour,
                                                  'album': appear_album,
                                                  'prev': prev,
                                                  'next': next,

                                          })
