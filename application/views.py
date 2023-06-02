from django.shortcuts import render, redirect
from .forms import*


def welcom(request):
    return render(request, 'welcome.html', {'title': 'Добро пожаловать!'})


def question(request):
    form = SendQuestionForm()
    title = 'Ваши вопросы'
    data = {
        'form': form,
        'title': title,
    }

    if request.method == 'POST':
        form = SendQuestionForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('success')     

    return render(request, 'form.html', data)


def teacher_app(request):
    form = SendTeacherAppForm()
    title = 'Анкета сотрудника'
    data = {
        'form': form,
        'title': title,
    }

    if request.method == 'POST':
        form = SendTeacherAppForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success')
    else:
        form = SendTeacherAppForm()

    return render(request, 'form.html', data)


def child_app(request):
    form = SendChildAppForm()
    title = 'Анкета ребёнка'
    data = {
        'form': form,
        'title': title,
    }

    if request.method == 'POST':
        form = SendChildAppForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success')
    else:
        form = SendChildAppForm()

    return render(request, 'form.html', data)


def success(request):
    return render(request, 'success.html', {'title': 'Успех!'})
