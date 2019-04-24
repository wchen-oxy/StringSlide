# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appearances(models.Model):
    guitar = models.ForeignKey('Guitar', models.DO_NOTHING, primary_key=True)
    tour_name = models.CharField(max_length=120, blank=True, null=True)
    album_name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Appearances'




class Guitar(models.Model):
    guitar_id = models.SmallIntegerField(primary_key=True)
    manufacturer_name = models.CharField(max_length=65, blank=True, null=True)
    guitar_name = models.CharField(max_length=80, blank=True, null=True)
    guitar_model = models.CharField(max_length=80, blank=True, null=True)
    serial_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Guitar'

    def __str__(self):
        template = '{0.guitar_id} {0.manufacturer_name} {0.guitar_model}'
        return template.format(self)


class Photos(models.Model):
    guitar = models.ForeignKey(Guitar, models.DO_NOTHING, primary_key=True)
    photo_number = models.IntegerField()
    photo_path = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Photos'
        unique_together = (('guitar', 'photo_number'),)





class Specs(models.Model):
    guitar = models.ForeignKey(Guitar, models.DO_NOTHING, primary_key=True)
    guitar_spec_id = models.SmallIntegerField()
    production_year = models.SmallIntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    finish = models.CharField(max_length=80, blank=True, null=True)
    body_wood = models.CharField(max_length=80, blank=True, null=True)
    neck_wood = models.CharField(max_length=80, blank=True, null=True)
    fretboard_wood = models.CharField(max_length=80, blank=True, null=True)
    cap_wood = models.CharField(max_length=80, blank=True, null=True)
    neck_pickup = models.CharField(max_length=80, blank=True, null=True)
    middle_pickup = models.CharField(max_length=80, blank=True, null=True)
    bridge_pickup = models.CharField(max_length=80, blank=True, null=True)
    repairs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Specs'
        unique_together = (('guitar', 'guitar_spec_id'),)


class Story(models.Model):
    story_id = models.SmallIntegerField()
    guitar = models.ForeignKey(Guitar, models.DO_NOTHING, primary_key=True)
    story_text = models.TextField()
    where_purchased = models.CharField(max_length=80, blank=True, null=True)
    custom_built = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Story'
        unique_together = (('guitar', 'story_id'),)


class Videos(models.Model):
    guitar = models.ForeignKey(Guitar, models.DO_NOTHING, primary_key=True)
    video_number = models.IntegerField()
    video_path = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Videos'
        unique_together = (('guitar', 'video_number'),)
