from django.contrib import admin
from .models import UserProfile, Job

admin.site.register(Job)
admin.site.register(UserProfile)
