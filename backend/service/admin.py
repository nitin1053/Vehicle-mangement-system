from django.contrib import admin

# Register your models here.
# backend/service/admin.py
from django.contrib import admin
from .models import Component, Vehicle, Repair

admin.site.register(Component)
admin.site.register(Vehicle)
admin.site.register(Repair)
