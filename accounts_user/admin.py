from django.contrib import admin
#  In here call / import all method from model.py for 
from .models import SodeshOwnerUser, SodeshEmployee, SornaliOwnerUser, SornaliEmployee

# in here register all method which is created in model.py . Actually this is give a view in admin pannel
 
admin.site.register(SodeshOwnerUser)
admin.site.register(SodeshEmployee)
admin.site.register(SornaliOwnerUser)
admin.site.register(SornaliEmployee)