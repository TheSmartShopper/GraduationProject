from django.contrib import admin

# Register your models here.
from .models import StoreAdminProfile,CustomerProfile

admin.site.register(StoreAdminProfile)
admin.site.register(CustomerProfile)