from rest_framework import serializers
from .models import Users, Events


# class EventOrginizers_Serializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = EventOrginizers
#         fields = ('event_id', 'user_id')
#         read_only_fields = ('event_id', 'user_id')

# class EventUsers_Serializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = EventUsers
#         fields = ('event_id', 'user_id', 'status')
#         read_only_fields = ('event_id', 'user_id', 'status')
#
class Events_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Events
        fields = ('id_event','title','location','date_time','price','tags', 'desctiption')
        read_only_fields = ()

class Users_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Users
        fields = ('id_user' ,'name','age','email','number','rating_plus', 'rating_minus', 'rating_zero', 'username')
        read_only_fields = ()
