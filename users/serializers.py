from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser, Profile
from station.utils import get_location
import decimal

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
       
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):

    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    
    class Meta:
        model = Profile
        fields = ['address', 'city', 'country', 'latitude', 'longitude']

    def update(self, instance, validated_data):

        if not validated_data.get('address'):
            raise serializers.ValidationError("Address Field should not be blank.")

        lat, lon = get_location(validated_data['address'])

        instance.latitude = float(lat)
        instance.longitude = float(lon)

        instance.address = validated_data['address']
        instance.city = validated_data['city']
        instance.country = validated_data['country']
        instance.save()

        return instance
