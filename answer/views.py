from django.shortcuts import render
from .forms import *
from application.models import *
from django.core.mail import send_mail
from kindergarten.settings import DEFAULT_FROM_EMAIL


def answer(request):
    questions = Question.objects.all()
    button_title = 'Отправить'

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
        'title': 'Ответить на вопрос или анкету',
        'button_title': button_title,
    }

    return render(request, 'answer.html', data)
