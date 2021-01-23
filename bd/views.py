from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Bangladesh
from django.contrib import messages
import re
from accounts_user.models import SwadeshOwnerUser,RiverParkModelTownOwnerUser,NewDhakaCityOwnerUser
from .models import Sodesh,NewDhakaCity,RiverParkModelTown,Swadesh

from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)


from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/owner_swadesh')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')

# Create your views here.


def bangladesh(request):
    bangladeshData = serialize('geojson', Bangladesh.objects.all())
    return HttpResponse(bangladeshData, content_type='geojson')

def sodesh(request):
    user = request.user
    sodeshData = serialize('geojson', Sodesh.objects.all())
    return HttpResponse(sodeshData, content_type='geojson')
# swadesh part
def swadesh(request):
    user = request.user
    swadeshData = serialize('geojson', Swadesh.objects.all())
    return HttpResponse(swadeshData, content_type='geojson')
def public_swadesh(request):
    user = request.user
    return render(request, 'public_swadesh.html')


def owner_swadesh(request):
    user = request.user
    swadeshOwnerUser =  SwadeshOwnerUser.objects.all()

    return render(request, 'owner_swadesh.html',locals())

def more_information_swadesh(request):
    user = request.user
    swadeshOwnerUser =  SwadeshOwnerUser.objects.all()
    swadeshData =  Swadesh.objects.all()
    fg = str(request.get_full_path)
    
    ft1 = str(re.findall("[0-9]", fg))
    ft2 = str(re.findall("[0-9][0-9]", fg))
    ft3 = str(re.findall("[0-9][0-9][0-9]", fg))
    x1 = '\n'.join(ft1)
    x2 = '\n'.join(ft2)
    x3 = '\n'.join(ft3)


    d1 = x1[4:5]
    d2_1 = x2[4:5]
    d2_2 = x2[6:7]
    d2 = d2_1 + d2_2
    d3_1 = x3[4:5]
    d3_2 = x3[6:7]
    d3_3 = x3[8:9]   
    d3 = d3_1 + d3_2 +d3_3

    if len(d3) > 2:
        sum = d3
    elif len(d2) > 1:
        sum = d2
    else:
        sum = d1


    

    return render(request, 'more_information_swadesh.html', locals())


# new dhaka city part
def new_dhaka_city(request):
    user = request.user
    new_dhaka_cityData = serialize('geojson', NewDhakaCity.objects.all())
    return HttpResponse(new_dhaka_cityData, content_type='geojson')


def public_new_dhaka_city(request):
    user = request.user

    return render(request, 'public_new_dhaka_city.html')


def owner_new_dhaka_city(request):
    user = request.user
    newDhakaCityOwnerUser =  NewDhakaCityOwnerUser.objects.all()
    return render(request, 'owner_new_dhaka_city.html', locals())

def more_information_new_dhaka_city(request):
    user = request.user
    newDhakaCityOwnerUser =  NewDhakaCityOwnerUser.objects.all()
    NewDhakaCityData =  NewDhakaCity.objects.all()
    fg = str(request.get_full_path)
    
    ft1 = str(re.findall("[0-9]", fg))
    ft2 = str(re.findall("[0-9][0-9]", fg))
    ft3 = str(re.findall("[0-9][0-9][0-9]", fg))
    x1 = '\n'.join(ft1)
    x2 = '\n'.join(ft2)
    x3 = '\n'.join(ft3)


    d1 = x1[4:5]
    d2_1 = x2[4:5]
    d2_2 = x2[6:7]
    d2 = d2_1 + d2_2
    d3_1 = x3[4:5]
    d3_2 = x3[6:7]
    d3_3 = x3[8:9]   
    d3 = d3_1 + d3_2 +d3_3

    if len(d3) > 2:
        sum = d3
    elif len(d2) > 1:
        sum = d2
    else:
        sum = d1


    

    return render(request, 'more_information_new_dhaka_city.html', locals())



def more_informationht(request):
    user = request.user
    return render(request, 'more_information.html')

# new river park model town part

def river_park_model_town(request):
    user = request.user
    river_park_model_townData = serialize('geojson', RiverParkModelTown.objects.all())
    return HttpResponse(river_park_model_townData, content_type='geojson')


def public_river_park_model_town(request):
    user = request.user

    return render(request, 'public_river_park_model_town.html')


def owner_river_park_model_town(request):
    user = request.user

    return render(request, 'owner_river_park_model_town.html')


def more_information_river_park_model_town(request):
    user = request.user
    riverParkModelTownOwnerUser = RiverParkModelTownOwnerUser.objects.all()
    RiverParkModelTownData =  RiverParkModelTown.objects.all()
    fg = str(request.get_full_path)
    
    ft1 = str(re.findall("[0-9]", fg))
    ft2 = str(re.findall("[0-9][0-9]", fg))
    ft3 = str(re.findall("[0-9][0-9][0-9]", fg))
    ft4 = str(re.findall("[0-9][0-9][0-9][0-9]", fg))
    x1 = '\n'.join(ft1)
    x2 = '\n'.join(ft2)
    x3 = '\n'.join(ft3)
    x4 = '\n'.join(ft4)


    d1 = x1[4:5]
    d2_1 = x2[4:5]
    d2_2 = x2[6:7]
    d2 = d2_1 + d2_2
    d3_1 = x3[4:5]
    d3_2 = x3[6:7]
    d3_3 = x3[8:9]
    d4_1 = x4[4:5]
    d4_2 = x4[6:7]
    d4_3 = x4[8:9]
    d4_4 = x4[10:11]   
    d3 = d3_1 + d3_2 +d3_3
    d4 = d4_1 +d4_2 + d4_3 + d4_4
    if len(d4) > 3:
        sum = d4
    elif len(d3) > 2:
        sum = d3
    elif len(d2) > 1:
        sum = d2
    else:
        sum = d1


    

    return render(request, 'more_information_river_park_model_town.html', locals())







def more_information(request):
    sodeshData =  Sodesh.objects.all()
    fg = str(request.get_full_path)
    
    ft1 = str(re.findall("[0-9]", fg))
    ft2 = str(re.findall("[0-9][0-9]", fg))
    ft3 = str(re.findall("[0-9][0-9][0-9]", fg))
    x1 = '\n'.join(ft1)
    x2 = '\n'.join(ft2)
    x3 = '\n'.join(ft3)


    d1 = x1[4:5]
    d2_1 = x2[4:5]
    d2_2 = x2[6:7]
    d2 = d2_1 + d2_2
    d3_1 = x3[4:5]
    d3_2 = x3[6:7]
    d3_3 = x3[8:9]   
    d3 = d3_1 + d3_2 +d3_3

    if len(d3) > 2:
        sum = d3
    elif len(d2) > 1:
        sum = d2
    else:
        sum = d1


    

    return render(request, 'more_information.html', locals())



def more_informationht(request):
    user = request.user
    return render(request, 'more_information.html')

def index(request):
    return render(request, 'index.html')



def  about_pims(request):
    user = request.user
    return render(request,'about_PIMS.html')




def  contact(request):
    user = request.user
    return render(request,'contact_us.html')
def pricing(request):
    user = request.user

    return render(request, 'pricing.html')

def home(request):

    return render(request, 'public_data.html')


def sodesh_home(request):

    return render(request, 'home_sodesh.html')



