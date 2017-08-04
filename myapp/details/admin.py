# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserDetails
from django.http import HttpResponse

from details.utils import render_to_pdf
from reportlab.pdfgen import canvas

# Register your models here.
class UserAdmin(admin.ModelAdmin):
 list_display = ["name","email",]
 fields = ["name","email","address","Gender","dob","AboveEighteen"]
 search_fields = ["name","email"]
  
 def response_change(self, request, obj):
	
    if '_saveaspdf' in request.POST:
        all={"Name":obj.name,
	     "Email":obj.email,
	     "Address":obj.address,
	     "DOB":obj.dob,
	     "Gender":obj.gender,
	     }  
        pdf = render_to_pdf('my_template.html', {"all":all})
        return HttpResponse(pdf, content_type='application/pdf')
    print all
#print PDF to response
  
	
admin.site.register(UserDetails,UserAdmin) 

