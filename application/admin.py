from django.contrib import admin

from .models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'phone_number',
        'text',
    ]
    list_per_page = 10


@admin.register(TeacherApplication)
class TeacherAppAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'phone_number',
        'specialization',
        'education',
        'experience',
    ]
    list_per_page = 10


@admin.register(AdaptiveApplication)
class AdaptiveAppAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'phone_number',
        'child_full_name',
    ]
    list_per_page = 10


@admin.register(ChildApplication)
class ChildAppAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 
        'email', 
        'phone_number', 
        'child_full_name', 
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
