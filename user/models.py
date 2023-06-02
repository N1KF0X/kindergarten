from django.db import models
from django.core.validators import RegexValidator


class Program(models.Model):
    name = models.CharField(
        verbose_name='Название программы',
        max_length=50,
    )
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Программа'
        verbose_name_plural='Программы'


class Child(models.Model):
    phone_number_regex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

    full_name = models.CharField(
        verbose_name='Ф.И.О.', 
        max_length=50,
    )
    age = models.IntegerField(verbose_name='Возраст')
    phone_number = models.CharField(
        verbose_name='Номер телефона родителя/опекуна', 
        max_length=14,
        validators = [phone_number_regex],
    )
    needs_a_psychologist = models.BooleanField(
        verbose_name='Нуждается в психологе',
    )
    needs_a_logopedist = models.BooleanField(
        verbose_name='Нуждается в логопеде',
    )
    program = models.ForeignKey(
        Program, 
        on_delete = models.CASCADE, 
        verbose_name='Группа',
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name='Ребёнок'
        verbose_name_plural='Дети'