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
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'phone_number',
        'specialization',
        'education',
        'experience',
    ]
    list_per_page = 10


@admin.register(ChildApplication)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'email',
        'phone_number',
        'age',
    ]
    list_per_page = 10
