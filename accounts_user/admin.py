from django.contrib import admin

from .models import SodeshOwnerUser, SodeshEmployee, SornaliOwnerUser, SornaliEmployee


admin.site.register(SodeshOwnerUser)
admin.site.register(SodeshEmployee)
admin.site.register(SornaliOwnerUser)
admin.site.register(SornaliEmployee)