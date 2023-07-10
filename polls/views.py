from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Contact
from django.core import serializers
import json
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect



def showtable(request):
    Cont = Contact.objects.all()
    return render(request, 'showtable.html',{
        'contacts' : Cont ,
    })
