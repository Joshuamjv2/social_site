from django.contrib import admin

from .models import Image
@admin.register(Image)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'image','created']

# Register your models here.


