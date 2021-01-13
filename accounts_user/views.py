from django.shortcuts import render

from django.core.serializers import serialize
from django.http import HttpResponse

from django.contrib import messages
import re



# Create your views here.
# In here calling  all method in this section from database which is model.py
from .models import SodeshOwnerUser,SornaliOwnerUser



# this is a view which is communicate database and htpage in this section
# all object goes t profile.html page which is play as like magic
def user_information(request):
    sodeshOwnerUser =  SodeshOwnerUser.objects.all()
    sornaliOwnerUser =  SornaliOwnerUser.objects.all()
    return render(request, 'profile.html', locals())