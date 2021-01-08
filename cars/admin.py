from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Color)
admin.site.register(Car)
admin.site.register(Client)
admin.site.register(ClientPassportData)
admin.site.register(Manager)
admin.site.register(Order)

