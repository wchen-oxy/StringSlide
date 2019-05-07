from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db import connection

import random
from .models import Guitar, Story, Photos, Specs, Appearances, Videos
from .forms import GuitarForm, AppearForm, PhotosForm, SpecsForm, StoryForm, VideosForm
from django.shortcuts import redirect
from django.forms.formsets import formset_factory




# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the entries")

def home(request):
    num = random.randint(1,1020)
    num2 = random.randint(1,1020)

    guitar = Guitar.objects.get(guitar_id=num)
    g_photo = Photos.objects.get(guitar=num)
    g_story = Story.objects.get(guitar_id=num)
    guitar2 = Guitar.objects.get(guitar_id=num2)
    g_photo2 = Photos.objects.get(guitar_id=num2)
    g_story2 = Story.objects.get(guitar_id=num2)
    guitar3 = Guitar.objects.get(guitar_id=1019)
    g_photo3 = Photos.objects.get(guitar=1019)
    g_story3 = Story.objects.get(guitar_id=1019)

    text_1 = g_story.story_text;
    text_1 = (text_1[:100] + '...') if len(text_1) > 103 else text_1
    text_2 = g_story2.story_text;
    text_2 = (text_2[:100] + '...') if len(text_2) > 103 else text_2
    text_3 = g_story3.story_text;
    text_3 = (text_3[:100] + '...') if len(text_3) > 103 else text_3


    return render(request, 'home.html', {'guitar_id': guitar.guitar_id,
                                         'guitar_manufacturer': guitar.manufacturer_name,
                                         'guitar_model': guitar.guitar_model,
                                         'guitar_name': guitar.guitar_name,
                                         'guitar_image' : g_photo.photo_path,
                                         'guitar_summary' : text_1,

                                         'guitar_id2': guitar2.guitar_id,
                                         'guitar_manufacturer2': guitar2.manufacturer_name,
                                         'guitar_model2': guitar2.guitar_model,
                                         'guitar_name2': guitar2.guitar_name,
                                         'guitar_image2' : g_photo2.photo_path,
                                         'guitar_summary2' : text_2,

                                         'guitar_id3': guitar3.guitar_id,
                                         'guitar_manufacturer3': guitar3.manufacturer_name,
                                         'guitar_model3': guitar3.guitar_model,
                                         'guitar_name3': guitar3.guitar_name,
                                         'guitar_image3' : g_photo3.photo_path,
                                         'guitar_summary3' : text_3,

                                         })

def new(request):
    data = None
    form = GuitarForm(request.POST)
    form2 = AppearForm(request.POST)
    form3 = PhotosForm(request.POST)
    form4 = SpecsForm(request.POST)
    form5 = StoryForm(request.POST)
    form6 = VideosForm(request.POST)
    print("begin")
    #section for submission
    if request.method == "POST":
        data = request.POST
        print("is Post")

        user = request.user
        post_values = request.POST.copy()

        #section for random guitar_id
        boo = True
        while boo:
            print("in while")
            num = random.randint(0, 9999)
            try:
                print("inner")
                print(Guitar.objects.get(guitar_id=num))
            except:
                print("exception occured")
                master_id = num
                boo = False
        #section for photo_id
        boo = True
        while boo:
            print("in while")
            num = random.randint(0, 127)
            try:
                print("inner")
                if not Photos.objects.get(photo_number=num):
                    print("inner")

            except:
                print("exception occured")
                photo_id = num
                boo = False

        #section for video id
        boo = True
        while boo:
            print("in while")
            num = random.randint(0, 127)
            try:
                print("inner")
                if not Videos.objects.get(video_number=num):
                    print("inner")

            except:
                print("exception occured")
                video_id = num
                boo = False
        #section for story_id
        boo = True
        while boo:
            print("in while")
            num = random.randint(0, 127)
            try:
                print("inner")
                if not Story.objects.get(story_id=num):
                    print("inner")

            except:
                print("exception occured")
                story_id = num
                boo = False
        # section for spec
        boo = True
        while boo:
            print("in while")
            num = random.randint(0, 127)
            try:
                print("inner")
                if not Specs.objects.get(guitar_spec_id=num):
                    print("inner")

            except:
                print("exception occured")
                spec_id = num
                boo = False
        print("while exited")

        post_values['guitar_id'] = str(master_id)
        print(post_values)
        # form = GuitarForm(post_values)
        print("1")
        guitar = GuitarForm(post_values, prefix="gui")
        print("2")
        appearances = AppearForm(request.POST, prefix="app")
        # if guitar.is_valid() and appearances.is_valid():
        form = GuitarForm(data)
        form2 = AppearForm(data)
        form3 = PhotosForm(data)
        form4 = SpecsForm(data)
        form5 = StoryForm(data)
        form6 = VideosForm(data)



        if guitar.is_valid() and appearances.is_valid():
            print(master_id)
            newitem = form.save(commit=False)
            newitem.guitar_id = master_id
            newitem.save()
            newitem = form2.save(commit=False)
            newitem.guitar_id = master_id
            newitem.save()
            newitem = form3.save(commit=False)
            newitem.guitar_id = master_id
            newitem.photo_number = photo_id
            newitem.save()
            newitem = form4.save(commit=False)
            newitem.guitar_id = master_id
            newitem.guitar_spec_id = spec_id
            newitem.save()
            newitem = form5.save(commit=False)
            newitem.guitar_id = master_id
            newitem.story_id = story_id
            newitem.save()
            newitem = form6.save(commit=False)
            newitem.guitar_id = master_id
            newitem.video_number = video_id
            newitem.save()

            print(newitem.guitar_id)
            return redirect('/entries/' + str(newitem.pk))
    #section for display
    else:
        print("outer")
        form = GuitarForm()
        form2 = AppearForm()
        form3 = PhotosForm()
        form4 = SpecsForm()
        form5 = StoryForm()
        form6 = VideosForm()
    return render(request, 'new_edit.html', {'form': form, 'form2': form2, 'form3': form3,
                                             'form4': form4, 'form5':form5, 'form6': form6})
    # return render(request, 'new_edit.html', {'form': form})



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
        repaired = "No repairs"



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
