"""gic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import home

from bd.views import login_view, register_view, logout_view, sodesh,sodesh_home,more_information,home,public_new_dhaka_city,owner_new_dhaka_city
from bd.views import public_river_park_model_town, owner_river_park_model_town,more_information_river_park_model_town, more_information_new_dhaka_city
from bd.views import swadesh,public_swadesh,owner_swadesh,more_information_swadesh
from accounts_user.views import user_information
from contacts.views import sodesh_contact,company_contact_to_admin
from django.conf.urls import url, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('bd.urls')),
    path('', include('accounts_user.urls')),
     path('', include('contacts.urls')),
    # path('detail/',home),
    path('accounts/login/', login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view),
    path('home/',home),
    path('sodeshDat/',sodesh_home),
    path('more_infortion/',more_information),
    #new dhaka city part
    path('public_new_dhaka_city/',public_new_dhaka_city),
    path('owner_new_dhaka_city/',owner_new_dhaka_city),
    path('more_information_new_dhaka_city/',more_information_new_dhaka_city),
    # river park model town part
    path('public_river_park_model_town/',public_river_park_model_town),
    path('owner_river_park_model_town/',owner_river_park_model_town),
    path('more_information_river_park_model_town/',more_information_river_park_model_town),
    # swadesh part
    path('public_swadesh/',public_swadesh),
    path('owner_swadesh/',owner_swadesh),
    path('more_information_swadesh/',more_information_swadesh),
# adminlte part
    url(r'^$', TemplateView.as_view(template_name='adminlte/index.html')),
    url(r'^login/$', TemplateView.as_view(template_name='adminlte/login.html')),
    path('admin/', admin.site.urls),

]
