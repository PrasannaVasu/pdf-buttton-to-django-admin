# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

# Create your models here.
Gender = (
    ('select', 'SELECT'),
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('O', 'OTHER'),
)
class UserDetails(models.Model):
 name = models.CharField(max_length=20)
 email = models.EmailField()
 address = models.CharField(max_length=80)
 Gender = models.CharField(max_length=20,choices=Gender,default='select')
 dob = models.DateField()
 AboveEighteen = models.BooleanField()
 
 def __str__(self):
    return self.name
	
 def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))
		
		
 