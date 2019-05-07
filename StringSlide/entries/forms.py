from django import forms
import random

from .models import Guitar, Story, Photos, Specs, Appearances, Videos

master_id = 0

class AppearForm(forms.ModelForm):
    Appearances.guitar_id = master_id
    tour_name = forms.CharField(required=False)
    album_name = forms.CharField(required=False)
    class Meta:
        model = Appearances
        fields = ('tour_name', 'album_name')

class GuitarForm(forms.ModelForm):
    # serial_number = forms.CharField(required=False)

    class Meta:
        model = Guitar
        fields = ("manufacturer_name", "guitar_name", "guitar_model", "serial_number")

class PhotosForm(forms.ModelForm):

    photo_path = forms.CharField(required=False)

    class Meta:
        model = Photos
        fields = ('photo_path',)

class SpecsForm(forms.ModelForm):

    # OPTIONS = (
    # ("1", 'True'),
    #     ("0", 'False'),
    #
    # )
    # repairs = forms.ChoiceField(widget=forms.CheckboxSelectMultiple,
    #                                  choices=OPTIONS)
    # print(repairs)
    class Meta:
        model = Specs
        # fields = '__all__'
        fields = ('production_year', 'weight', 'finish',
                  'body_wood', 'neck_wood', 'fretboard_wood', 'cap_wood', 'neck_pickup',
                  'middle_pickup', 'bridge_pickup', 'repairs')

class StoryForm(forms.ModelForm):
    where_purchased = forms.CharField(label='Current Location', required=False)
    # story_text = forms.CharField(widget=forms.Textarea, required=False)
    # custom_built = forms.IntegerField(required=False)
    class Meta:
        model = Story
        fields = ('where_purchased', 'custom_built', 'story_text')

class VideosForm(forms.ModelForm):
    video_path = forms.CharField(required=False)
    class Meta:
        model = Videos
        fields = ('video_path',)



