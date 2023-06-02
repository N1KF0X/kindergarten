from django.contrib import admin
from django.urls import path
from application.views import *
from user.views import *
from answer.views import *

admin.site.site_header = 'Детский садик [Название]'
admin.site.index_title = 'Детский садик [Название] - Администрирование'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcom, name='home'),
    path('success/', success, name='success'),
    path('question/', question, name='question'),
    path('teacher_app/', teacher_app, name='teacher_app'),
    path('child_app/', child_app, name='child_app'),
    path('login/', Login.as_view(), name='login'),
    path('children/', ChildList.as_view(), name='children'),
    path('answer_the_question/', answer_the_question, name='answer_the_question'),
     path("logout/", logout_user, name = "logout"),
    #path('answer_the_tapp/', answer_the_tapp, name='answer_the_tapp'),
    #path('answer_the_capp/', answer_the_capp, name='answer_the_capp'),
]
