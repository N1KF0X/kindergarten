from django.shortcuts import render
from .forms import *
from application.models import *
from django.core.mail import send_mail
from kindergarten.settings import DEFAULT_FROM_EMAIL

def answer_the_question(request):
    questions = Question.objects.all()

    if request.method == 'GET':
        form = AnswerForm()
    elif request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            subject = 'Ответ от даминистрации садика'
            message = form.cleaned_data['answer_text']
            email = [form.cleaned_data['email']]
            send_mail(
                subject, 
                message,
                DEFAULT_FROM_EMAIL,
                email,
            )

    data = {
        'questions': questions,
        'form': form,
        'title': 'Ответить на вопрос или анкету'
    }

    return render(request, 'answer_the_question.html', data)


def answer_the_tapp(request):
    questions = TeacherApplication.objects.all()

    if request.method == 'GET':
        form = AnswerForm()
    elif request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            subject = 'Ответ от даминистрации садика'
            message = form.cleaned_data['answer_text']
            email = [form.cleaned_data['email']]
            send_mail(
                subject, 
                message,
                DEFAULT_FROM_EMAIL,
                email,
            )

    data = {
        'questions': questions,
        'form': form,
    }

    return render(request, 'answer_the_tapp.html', data)


def answer_the_capp(request):
    questions = ChildApplication.objects.all()

    if request.method == 'GET':
        form = AnswerForm()
    elif request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            subject = 'Ответ от даминистрации садика'
            message = form.cleaned_data['answer_text']
            email = [form.cleaned_data['email']]
            send_mail(
                subject, 
                message,
                DEFAULT_FROM_EMAIL,
                email,
            )

    data = {
        'questions': questions,
        'form': form,
    }

    return render(request, 'answer_the_qapp.html', data)
