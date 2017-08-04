# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import get_template
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.db import models
from details.utils import render_to_pdf #created in step 4
from .models import UserDetails
class GeneratePdf(View): 
     def get(self, request, *args, **kwargs):
         all={"Name":"obj.name",
	     "Email":"obj.email",
	     "Address":"obj.address",
	     "DOB":"obj.dob",
	     "Gender":"obj.gender",
	     } 
         pdf = render_to_pdf('my_template.html', {"all":all})
         return HttpResponse(pdf, content_type='application/pdf')