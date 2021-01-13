from django.contrib import admin
from .models import Bangladesh,Sodesh
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

# list_display is visulize column field in admin pannel
#list_filter is give a button in admin pannel which is give great flexibility for filtering
#list_editable is a option which gives a clear editable field without entering deep
class BangladeshAdmin(LeafletGeoAdmin):
    list_display = ['adm2_en','adm1_en','shape_leng','date']
    list_filter = ['shape_leng','adm1_en']
    list_editable = ['date']

class SodeshAdmin(LeafletGeoAdmin):
    list_display = ['area_k','katha','plot_no','land_cat']
    # list_filter = ['shape_leng','adm1_en']
    # list_editable = ['date']

admin.site.register(Bangladesh,BangladeshAdmin)
admin.site.register(Sodesh, SodeshAdmin)





























