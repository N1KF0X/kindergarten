from django.views.generic import ListView
from django.shortcuts import render

from .models import *

class Teachers(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    extra_context = {
        'title': 'Детский сад "Фантазия": Педагоги',
        'header': "Наши педагоги",
    }

