from django.shortcuts import render

from django.core.serializers import serialize
from django.http import HttpResponse

from django.contrib import messages
import re








# Create your views here.
from .models import SodeshOwnerUser,SornaliOwnerUser


def user_information(request):
    sodeshOwnerUser =  SodeshOwnerUser.objects.all()
    sornaliOwnerUser =  SornaliOwnerUser.objects.all()
    return render(request, 'profile.html', locals())