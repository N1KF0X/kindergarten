from django.shortcuts import redirect

from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import *
from .models import Child
from django.contrib.auth import logout

class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    extra_context = {
        'title': 'Войти как педагог',
        'button_title': 'Войти',
    }

    def get_success_url(self):
        return reverse_lazy('children')


class ChildList(ListView):
    model = Child
    template_name = 'children.html'
    context_object_name = 'children'
    extra_context = {'title': 'Группа'}


def logout_user(request):
    logout(request)
    return redirect('login')
