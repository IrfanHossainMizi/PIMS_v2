from django.urls import path
from .views import sodesh_contact,company_contact_to_admin
from .views import swadesh_contact, newDhakaCity_contact, riverParkModelTown_contact
urlpatterns = [
    path('sodesh_contact', sodesh_contact, name = 'sodesh_contact'),
    path('swadesh_contact', swadesh_contact, name = 'swadesh_contact'),
    path('newDhakaCity_contact', newDhakaCity_contact, name = 'newDhakaCity_contact'),
    path('riverParkModelTown_contact', riverParkModelTown_contact, name = 'riverParkModelTown_contact'),
    path('company_contact_to_admin', company_contact_to_admin, name = 'company_contact_to_admin'),

]