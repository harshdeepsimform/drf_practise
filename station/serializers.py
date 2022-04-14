from attr import validate
from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Station, Slot


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ['name', 'address', 'city', 'country']

    def create(self, validated_data):
        # user = Station(
        #     name = 


        #     email=validated_data['email'],
        #     username=validated_data['username']
        # )
        # user.set_password(validated_data['password'])
        # user.save()
        # return user
        return validated_data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['url', 'name']
