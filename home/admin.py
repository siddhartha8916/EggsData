from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Csvs)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'filename', 'uploaded','activated']

@admin.register(egg_monthly_price)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'market', 'arrival_date','price','created_at']