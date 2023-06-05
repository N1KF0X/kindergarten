from django.shortcuts import render, redirect
from .forms import*


button_title = 'Отправить'
app_template = 'app.html'


def home(request):
    form = SendAdaptiveAppForm()
    data = {
        'form': form,
        'title': 'Детский сад "Фантазия"',
        'header': 'Добро пожаловать!',
        'button_title': button_title,
    }
    return render(request, 'welcome.html', data)


def question(request):
    form = SendQuestionForm()
    title = 'Ваши вопросы'
    data = {
        'form': form,
        'title': title,
        'header': title,
        'button_title': button_title,
    }

    if request.method == 'POST':
        form = SendQuestionForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('success')     

    return render(request, app_template, data)


def teacher_app(request):
    form = SendTeacherAppForm()
    title = 'Анкета сотрудника'
    data = {
        'form': form,
        'title': title,
        'header': title,
        'button_title': button_title,
    }

    if request.method == 'POST':
        form = SendTeacherAppForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success')
    else:
        form = SendTeacherAppForm()

    return render(request, app_template, data)


def child_app(request):
    form = SendChildAppForm()
    title = 'Запись ребёнка в группу'
    data = {
        'form': form,
        'title': title,
        'header': title,
        'button_title': button_title,
    }

    if request.method == 'POST':
        form = SendChildAppForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success')
    else:
        form = SendChildAppForm()

    return render(request, app_template, data)


def success(request):
    title = 'Успех!'
    data = {
        'title': title,
        'header': title,
    }
    return render(request, 'success.html', )
