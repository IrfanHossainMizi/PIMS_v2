from django.urls import path
from .views import sodesh_contact,company_contact_to_admin

urlpatterns = [
    path('sodesh_contact', sodesh_contact, name = 'sodesh_contact'),
    path('company_contact_to_admin', company_contact_to_admin, name = 'company_contact_to_admin'),

]