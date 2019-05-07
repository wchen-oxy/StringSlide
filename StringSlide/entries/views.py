from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db import connection

import random
from .models import Guitar, Story, Photos, Specs, Appearances, Videos
from .forms import GuitarForm, AppearForm, PhotosForm, SpecsForm, StoryForm, VideosForm
from django.shortcuts import redirect
from django.db.models import Max

from django.forms.formsets import formset_factory
from django.db import connection

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]



# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the entries")

def home(request):
    num = random.randint(999,1020)
    num2 = random.randint(999,1020)
    num3 = random.randint(999,1020)
    num4 = random.randint(1,998)


    guitar = Guitar.objects.get(guitar_id=num)
    g_photo = Photos.objects.get(guitar=num)
    g_story = Story.objects.get(guitar_id=num4)
    guitar2 = Guitar.objects.get(guitar_id=num2)
    g_photo2 = Photos.objects.get(guitar_id=num2)
    g_story2 = Story.objects.get(guitar_id=num4)
    guitar3 = Guitar.objects.get(guitar_id=num3)
    g_photo3 = Photos.objects.get(guitar=num3)
    g_story3 = Story.objects.get(guitar_id=num4)

    text_1 = g_story.story_text;
    text_1 = (text_1[:100] + '...') if len(text_1) > 103 else text_1
    text_2 = g_story2.story_text;
    text_2 = (text_2[:100] + '...') if len(text_2) > 103 else text_2
    text_3 = g_story3.story_text;
    text_3 = (text_3[:100] + '...') if len(text_3) > 103 else text_3

    guitar_url = "/entries/" + str(guitar.guitar_id)
    guitar_url2 = "/entries/" + str(guitar2.guitar_id)
    guitar_url3 = "/entries/" + str(guitar3.guitar_id)



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


                                        'guitar_url': guitar_url,
                                        'guitar_url2': guitar_url2,
                                        'guitar_url3': guitar_url3

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
        print(Guitar.objects.all().aggregate(Max('guitar_id')))
        max_num = guitar_id=Guitar.objects.all().aggregate(Max('guitar_id'))['guitar_id__max']
        print(max_num)
        master_id = int(max_num) + 1
        # boo = True
        # while boo:
        #     print("in while guitar_id")
        #     num = random.randint(0, 9999)
        #     try:
        #         print("inner")
        #         print(Guitar.objects.get(guitar_id=num))
        #     except:
        #         print("exception occured")
        #         master_id = num
        #         boo = False
        #section for photo_id
        boo = True
        while boo:
            print("in while Photo id")
            num = random.randint(0, 127)

            photo_id = num
            boo = False

        #section for video id
        boo = True
        while boo:
            print("in while video id")
            num = random.randint(0, 127)

            video_id = num
            boo = False
        #section for story_id
        boo = True
        while boo:
            print("in while story id")
            num = random.randint(0, 127)

            story_id = num
            boo = False
        # section for spec
        boo = True
        while boo:
            print("in while spec id")
            num = random.randint(0, 127)

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
    # if 'q' in request.POST:
    #     guitar_id = request.GET['q']
    #
    #     guitar = Guitar.objects.get(guitar_id=guitar_id)
    #     story = Story.objects.get(guitar_id=guitar_id)
    #     photo = Photos.objects.get(guitar_id=guitar_id)
    #     spec = Specs.objects.get(guitar_id=guitar_id)
    #     try:
    #         appear_tour = Appearances.objects.get(guitar_id=guitar_id).tour_name
    #     except:
    #         appear_tour = "None"
    #
    #     try:
    #         appear_album = Appearances.objects.get(guitar_id=guitar_id).album_name
    #     except:
    #         appear_album = "None"
    #
    #     if int(guitar.guitar_id) != 1:
    #         prev = "/entries/" + str(int(guitar.guitar_id) - 1)
    #         next = "/entries/" + str(int(guitar.guitar_id) + 1)
    #     else:
    #         prev = "/entries/" + str(1)
    #         next = "/entries/" + str(int(guitar.guitar_id) + 1)
    #
    #     if spec.repairs == 1:
    #         repaired = "Yes"
    #     else:
    #         repaired = "No repairs"
    #
    #     return render(request, 'entries/entry.html', {'guitar_id': guitar.guitar_id,
    #                                                   'guitar_man': guitar.manufacturer_name,
    #                                                   'guitar_model': guitar.guitar_model,
    #                                                   'guitar_name': guitar.guitar_name,
    #                                                   'story': story.story_text,
    #                                                   'photo': photo.photo_path,
    #                                                   'production_year': spec.production_year,
    #                                                   'finish': spec.finish,
    #                                                   'weight': spec.weight,
    #                                                   'body_wood': spec.body_wood,
    #                                                   'neck_wood': spec.neck_wood,
    #                                                   'fretboard_wood': spec.fretboard_wood,
    #                                                   'cap_wood': spec.cap_wood,
    #                                                   'neck_pick': spec.neck_pickup,
    #                                                   'middle_pickup': spec.middle_pickup,
    #                                                   'bridge_pickup': spec.bridge_pickup,
    #                                                   'repairs': repaired,
    #                                                   'tour': appear_tour,
    #                                                   'album': appear_album,
    #                                                   'prev': prev,
    #                                                   'next': next,
    #
    #                                                   })       # return render(request, 'entries', {'error': error})

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


def search(request):
    print("Made it !")
    print(request)
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        exact_entry = Guitar.objects.filter(guitar_model__iexact=q)
        entrys = Guitar.objects.filter(guitar_model__icontains=q)
        return render(request, 'entries/entry_list.html', {'entrys': entrys, 'query': exact_entry})
        # return render(request, 'entries', {'error': error})
    return HttpResponse("Error")


def advsearch(request):

    if 'prod_year' in request.GET:
        manufacturer = request.GET['prod_year']
        Query = "Select manufacturer_name, guitar_model, " \
            "guitar_name, production_year, g.guitar_id from Story s inner join Guitar g " \
            "on s.guitar_id=g.guitar_id inner join Specs t on " \
            "g.guitar_id=t.guitar_id where production_year= %s"
        with connection.cursor() as cursor:
            cursor.execute(Query, [manufacturer])
            row = dictfetchall(cursor)
            return render(request, 'entries/entry_list.html', {'prod_year_result': row})

    if 'manufacturer_name' in request.GET and 'era' in request.GET:
        manufacturer_name = request.GET['manufacturer_name']
        era = request.GET['era']
        era_string = era[:-2] + "%"
        Query = "select manufacturer_name, guitar_name, guitar_model, g.guitar_id, production_year, where_purchased " \
                "from guitar g inner join specs s on g.guitar_id=s.guitar_id" \
                " inner join story t on s.guitar_id=t.guitar_id" \
                " where s.production_year like %s and g.manufacturer_name= %s"
        with connection.cursor() as cursor:
            cursor.execute(Query, [era_string, manufacturer_name])
            row = dictfetchall(cursor)
            print(row)
            return render(request, 'entries/entry_list.html', {'man_era_result': row})

    if 'current_country' in request.GET and 'prod_year_country' in request.GET:
        print("I MADE IT")
        current_country = request.GET['current_country']
        prod_year = request.GET['prod_year_country']
        current_country_string = "%"+current_country+"%"
        Query = "Select manufacturer_name, guitar_model, guitar_name, production_year, where_purchased, s.guitar_id " \
                "from Story s inner join Guitar g on s.guitar_id=g.guitar_id " \
                "inner join Specs t on g.guitar_id=t.guitar_id " \
                "where where_purchased like %s and production_year<%s"
        with connection.cursor() as cursor:
            cursor.execute(Query, [current_country_string, prod_year])
            row = dictfetchall(cursor)
            print(row)
            return render(request, 'entries/entry_list.html', {'country_prod_year': row})

    if 'n_pickup' in request.GET and 'm_pickup' in request.GET and 'b_pickup':
        n_pickup = request.GET['n_pickup']
        m_pickup = request.GET['m_pickup']
        b_pickup = request.GET['b_pickup']
        Query = "select s.guitar_id, manufacturer_name, guitar_name, guitar_model, production_year, neck_pickup, middle_pickup, bridge_pickup " \
                "from guitar g inner join specs s on g.guitar_id=s.guitar_id " \
                "where (neck_pickup=%s and middle_pickup=%s and bridge_pickup=%s)"
        with connection.cursor() as cursor:
            cursor.execute(Query, [n_pickup,m_pickup,b_pickup])
            row = dictfetchall(cursor)
            print(row)
            return render(request, 'entries/entry_list.html', {'pickup_result': row})
    return HttpResponse("No Matches.")
