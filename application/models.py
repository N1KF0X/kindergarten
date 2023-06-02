from django.db import models
from django.core.validators import RegexValidator

class Application(models.Model):
    phone_number_regex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

    email = models.EmailField(verbose_name="Электронная почта")
    full_name = models.CharField(
        verbose_name="Ваше Ф.И.О.", 
        max_length=50,
    )    
    phone_number = models.CharField(
        verbose_name='Номер телефона', 
        max_length=14,
        validators = [phone_number_regex],
    )

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True
    

class Question(Application):
    text = models.TextField(verbose_name="Что Вас интересует:")
    
    class Meta:
        verbose_name='Вопрос'
        verbose_name_plural='Вопросы'

class TeacherApplication(Application):
    specialization = [
        ('В', 'Воспитатель'),
        ('ПВ', 'Помощник воспитателя'),
        ('ПДО', 'Педагог доп. образования'),
        ('С', 'Спец'),
        ('Д', 'Другое'),
    ]
    educations = [
        ('ОО', 'Основное общее'),
        ('СО', 'Среднее общее'),
        ('СП', 'Среднее проф.'),
        ('В', 'Высшее'),
    ]

    education = models.CharField(
        verbose_name='Образование',
        max_length=3,
        choices=educations,
    ) 
    experience = models.IntegerField(verbose_name='Стаж работы')
    specialization = models.CharField(
        verbose_name='Специальность',
        max_length=3,
        choices=specialization,
    )
    about_me = models.TextField(
        verbose_name='О себе',
        blank=True
    )

    class Meta:
        verbose_name='Заявка на трудоустройство'
        verbose_name_plural='Заявки на трудоустройство'


class ChildApplication(Application):
    age = models.IntegerField(verbose_name='Возраст ребёнка')
    child_full_name = models.CharField(
        verbose_name="Ф.И.О. ребёнка", 
        max_length=50,
    )
    need_in_logopedist = models.BooleanField(verbose_name='Нужен логопед')
    need_in_psychologist = models.BooleanField(verbose_name='Нужен психолог')

    class Meta:
        verbose_name='Заявка на посесещение садика'
        verbose_name_plural='Заявки на посесещения садика'
