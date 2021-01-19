from django.contrib import admin
#  In here call / import all method from model.py for 
from .models import SodeshOwnerUser, SodeshEmployee, SornaliOwnerUser, SornaliEmployee
from .models import NewDhakaCityOwnerUser, NewDhakaCityEmployee
from .models import SwadeshOwnerUser, SwadeshEmployee
from .models import RiverParkModelTownOwnerUser, RiverParkModelTownEmployee
# in here register all method which is created in model.py . Actually this is give a view in admin pannel
 
admin.site.register(SodeshOwnerUser)
admin.site.register(SodeshEmployee)
admin.site.register(SornaliOwnerUser)
admin.site.register(SornaliEmployee)
# sadesh part
admin.site.register(SwadeshOwnerUser)
admin.site.register(SwadeshEmployee)
# new dhaka city part 
admin.site.register(NewDhakaCityOwnerUser)
admin.site.register(NewDhakaCityEmployee)
# river park modeltown part 
admin.site.register(RiverParkModelTownOwnerUser)
admin.site.register(RiverParkModelTownEmployee)