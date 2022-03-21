import datetime
from httpx import delete
from pyexpat import model
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext as _



ROLE = ((1, "employer"), (2, "job_seeker"))
STATUS = ((0, "inactive"), (1, "active"))

YEAR = list((r,r) for r in range(1984, datetime.date.today().year+1))

def current_year():
    return datetime.date.today().year

class UserProfile(models.Model):
  user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  picture = models.ImageField(upload_to='images/users', null=True, verbose_name="")
  b_date = models.IntegerField(choices=YEAR, default=current_year)
  phone_number = models.IntegerField(unique=True)  
  code = models.IntegerField(unique=True)
  status = models.IntegerField(choices=STATUS, default=0)  
  role = models.IntegerField(choices=ROLE, default=0)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  deleted_on = models.DateTimeField(auto_now=True)


  def get_absolute_url(self):
        return reverse('main') 

  def __str__(self):
    return str(self.user_id)


class Job(models.Model):
  user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  title =  models.CharField(_('title'), max_length=200, unique=True)
  slug = models.SlugField(_('slug'), max_length=50)
  picture = models.ImageField(upload_to='images/jobs', null=True, verbose_name="")
  text = models.TextField(_('text'),)
  address = models.CharField(_('address'), max_length=200)
  location = models.CharField(max_length=500)
  status = models.IntegerField(choices=STATUS,default=0)  
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  deleted_on = models.DateTimeField(auto_now=True)
  

  def __str__(self):
    return self.title

  
  def get_absolute_url(self):
        return reverse('main')


