
from django.urls import path
from .views import home,index, bangladesh, sodesh,pricing,about_pims, contact,new_dhaka_city,public_new_dhaka_city,owner_new_dhaka_city
from .views import river_park_model_town,public_river_park_model_town,owner_river_park_model_town
from .views import swadesh,public_swadesh,owner_swadesh
urlpatterns = [

    path('', index, name = 'index'),
    path('home', home, name = 'home'),
    path('pricing', pricing, name = 'pricing'),
    path('bangladeshData', bangladesh, name='bangladeshData'),
    path('sodeshData', sodesh, name='sodeshData'),
# new dhaka city part
    path('new_dhaka_cityData',new_dhaka_city,name='new_dhaka_cityData'),
    path('public_new_dhaka_city', public_new_dhaka_city, name='public_new_dhaka_'),
    path('owner_new_dhaka_city', owner_new_dhaka_city, name='owner_new_dhaka_city'),
# river_park_model_town
    path('river_park_model_townData',river_park_model_town,name='river_park_model_townData'),
    path('public_river_park_model_town', public_river_park_model_town, name='public_river_park_model_town'),
    path('owner_river_park_model_town', owner_river_park_model_town, name='owner_river_park_model_town'),
# swadesh part
    path('swadeshData',swadesh,name='swadeshData'),
    path('public_swadesh', public_swadesh, name='public_swadesh'),
    path('owner_swadesh', owner_swadesh, name='owner_swadesh'),
    #other
    path('about_pims',about_pims,name='about_pims'),
    path('contact',contact,name='contact'),
    path('contact',contact,name='contact'),
]