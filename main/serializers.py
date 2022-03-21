from django.contrib.auth.models import User, Group
from .models import UserProfile, Job
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_id', 'picture', 'b_date', 'phone_number', 'code', 'status', 'role', 'created_on']    

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['user_id', 'title', 'slug', 'text', 'address', 'location', 'picture',  'status', 'created_on']                


