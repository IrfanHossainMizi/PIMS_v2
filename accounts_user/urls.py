
from django.urls import path
from .views import user_information

urlpatterns = [
    path('profile', user_information, name = 'profile'),

]