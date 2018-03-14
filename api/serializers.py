from rest_framework import serializers
from .models import Users, Events, EventUsers

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
class EventUsers_Serializer(serializers.ModelSerializer):

    class Meta:
        model = EventUsers
        fields = ('id_event','id_user','status', 'organizer', 'initializer')

class EventUsers_Serializer_For(serializers.ModelSerializer):

    class Meta:
        model = EventUsers
        fields = ('id_user','status', 'organizer', 'initializer')

class Events_Serializer(serializers.ModelSerializer):

    eventusers = EventUsers_Serializer_For(many=True)

    class Meta:
        model = Events
        fields = ('id_event','title','location','date_time','price','tags', 'desctiption', 'eventusers')

    def create(self, validated_data):
        profile_data = validated_data.pop('eventusers')
        id_event = Events.objects.create(**validated_data)
        for profile_data in profile_data:
            EventUsers.objects.create(id_event=id_event, **profile_data)
        return id_event


class Users_Serializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Users
        fields = ('id_user' ,'name','age','email','number','rating_plus', 'rating_minus', 'rating_zero', 'username')

class Events_Serializer_Time(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ('id_event','title','location','date_time','price','tags', 'desctiption')




