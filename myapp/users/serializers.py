from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'gender', 'image')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        profile = ProfileSerializer()
        fields = ('id', 'url', 'email', 'username', )

# class ProfileSerializer(serializers.HyperlinkModelSerializer):
#     class Meta:
#         model=Profile
#         fields = ('')
