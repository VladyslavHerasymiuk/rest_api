from rest_framework import serializers
from .models import Users\
    #EventOrginizers\
    #,EventUsers,Users,Events

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
# class Events_Serializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Events
#         fields = ('id','initializer','location','date','time','title')
#         read_only_fields = ('id','initializer','location','date','time','title')
#
class Users_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('id' ,'name','age','email','number')
        read_only_fields = ()