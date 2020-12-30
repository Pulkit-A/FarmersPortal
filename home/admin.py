from django.contrib import admin
from .models import CropOrder


class CropOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'productID', 'cost', 'qty')

admin.site.register(CropOrder, CropOrderAdmin)
