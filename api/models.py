# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AfterEvent(models.Model):
    id_event = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    id_user = models.IntegerField()
    imperessions = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'after_event'
        unique_together = (('id_event', 'id_user'),)


class EventUsers(models.Model):
    id_event = models.ForeignKey('Events', models.DO_NOTHING, db_column='id_event', primary_key=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')
    status = models.TextField(blank=True, null=True)
    organizer = models.IntegerField(blank=True, null=True)
    initializer = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'event_users'
        unique_together = (('id_event', 'id_user'),)


class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=60, blank=True, null=True)
    desctiption = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'events'


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    rating_plus = models.IntegerField(blank=True, null=True)
    rating_minus = models.IntegerField(blank=True, null=True)
    rating_zero = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'users'
