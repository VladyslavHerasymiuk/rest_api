from django.db import models


# class EventOrginizers(models.Model):
#     event_id = models.BigIntegerField(primary_key=True)
#     user_id = models.BigIntegerField()
#
#     class Meta:
#         db_table = 'event_orginizers'
#         unique_together = (('event_id', 'user_id'),)
#
#     def __str__(self):
#         return "{}".format(self.event_id)


#
# class EventUsers(models.Model):
#     event_id = models.BigIntegerField(primary_key=True)
#     user_id = models.BigIntegerField()
#     status = models.IntegerField()
#
#     class Meta:
#         db_table = 'event_users'
#         unique_together = (('event_id', 'user_id'),)
#
#     def __str__(self):
#         return "{}".format(self.event_id)
#
#
# class Events(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     initializer = models.BigIntegerField()
#     location = models.CharField(max_length=100)
#     date = models.DateField(auto_now=True)
#     time = models.TimeField(auto_now=True)
#     title = models.CharField(max_length=200)
#
#     class Meta:
#         db_table = 'events'
#
#     def __str__(self):
#         return "{}".format(self.id)

class Users(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    number = models.BigIntegerField()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return "{}".format(self.name)
