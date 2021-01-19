from django.contrib import admin

from .models import Contact_sodesh,Contact_from_compnay
from .models import Contact_NewDhakaCity, Contact_Swadesh,Contact_RiverParkModelTown


admin.site.register(Contact_sodesh)
admin.site.register(Contact_from_compnay)

admin.site.register(Contact_NewDhakaCity)
admin.site.register(Contact_Swadesh)
admin.site.register(Contact_RiverParkModelTown)