
from django.urls import path
from .views import user_information


#  I here user_infomation comes from view.py file and its url path is 'profile'
urlpatterns = [
    path('profile', user_information, name = 'profile'),

]