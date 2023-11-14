from django.contrib import admin
from .models import farmer
from .models import sell_animal
from .models import buy


admin.site.register(farmer)
admin.site.register(sell_animal)
admin.site.register(buy)


# Register your models here.
