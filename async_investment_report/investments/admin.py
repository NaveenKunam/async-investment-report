from django.contrib import admin
from .models import Investor, Property, Investment

admin.site.register(Investor)
admin.site.register(Property)
admin.site.register(Investment)
