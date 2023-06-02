from django.contrib import admin

from .models import *

admin.site.register(Program)

@admin.register(Child)
class Child(admin.ModelAdmin):
    list_display = [
        'full_name',
        'age',
        'needs_a_logopedist',
        'needs_a_psychologist',
        'program',
        'phone_number',
    ]
    list_per_page = 10
