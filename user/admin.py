from django.contrib import admin

from .models import *


@admin.register(Child)
class Child(admin.ModelAdmin):
    list_display = [
        'full_name', 
        'phone_number', 
        'orientation_of_education', 
        'art_club',
        'dance_club',
        'music',
        'physical_culture_club',
        'needlework_club',
        'robotics',
        'foreign_languages',
        'specialist_service',
    ]
    list_per_page = 10
