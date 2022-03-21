from django.contrib.auth.models import User, Group
from .models import UserProfile, Job
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, UserProfileSerializer, JobSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):    
    queryset = UserProfile.objects.order_by('-created_on')
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]   

class JobViewSet(viewsets.ModelViewSet):    
    queryset = Job.objects.order_by('-created_on')
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]        