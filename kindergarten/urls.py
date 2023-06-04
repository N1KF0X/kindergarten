from django.contrib import admin
from django.urls import path
from application.views import *
from user.views import *
from answer.views import *
from teachers.views import *
from django.conf.urls.static import static
from kindergarten import settings


admin.site.site_header = 'Детский садик [Название]'
admin.site.index_title = 'Детский садик [Название] - Администрирование'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('success/', success, name='success'),
    path('question/', question, name='question'),
    path('teacher_app/', teacher_app, name='teacher_app'),
    path('child_app/', child_app, name='child_app'),
    path('login/', Login.as_view(), name='login'),
    path('children/', ChildList.as_view(), name='children'),
    path('answer/', answer, name='answer'),
    path("logout/", logout_user, name = "logout"),
    path("teachers/", Teachers.as_view(), name = "teachers"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT,
    )