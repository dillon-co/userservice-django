from rest_framework import serializers
from .models import Demographics
from users.models import Profile
from django.contrib.auth.models import User

class DemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographics
        fields = ('male_count', 'female_count', 'other_count')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'gender', 'image')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        profile = ProfileSerializer()
        fields = ('id', 'url', 'email', 'username', 'first_name', 'last_name', 'profile')
