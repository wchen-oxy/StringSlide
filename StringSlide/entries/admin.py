from django.contrib import admin
from .models import Appearances, Guitar, Photos, Specs, Story

#Admin columns class
class PageAdmin(admin.ModelAdmin):
    list_display = ('guitar_id', 'manufacturer_name', 'guitar_name', 'guitar_model')
    #list_display_links = ('guitar_id', 'guitar_name', 'guitar_model')
    search_fields = ('guitar_id', 'manufacturer_name', 'guitar_name', 'guitar_model')
    list_per_page = 25

class SpecsInLine(admin.TabularInline):
    model = Specs

class GuitarInLine(admin.ModelAdmin):
    inlines = [SpecsInLine]



# Register your models here.
admin.site.register(Guitar, PageAdmin)




