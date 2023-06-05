from django.db import models


class Teacher(models.Model):
    specialization = [
        ('Воспитатель', 'Воспитатель'),
        ('Помощник воспитателя', 'Помощник воспитателя'),
        ('Педагог доп. образования', 'Педагог доп. образования'),
        ('Спец', 'Спец'),
    ]
    educations = [
        ('Основное общее', 'Основное общее'),
        ('Среднее общее', 'Среднее общее'),
        ('Среднее проф.', 'Среднее проф.'),
        ('Высшее', 'Высшее'),
    ]

    full_name = models.CharField(
        verbose_name='Ф.И.О.',
        max_length=50,
    )
    specialization = models.CharField(
        verbose_name='Специальность',
        max_length=50,
        choices=specialization,
    )
    education = models.CharField(
        verbose_name='Образование',
        max_length=50,
        choices=educations,
    )
    experience = models.IntegerField(verbose_name='Стаж работы')
    quote = models.CharField(
        verbose_name='Цитата',
        max_length=100,
        )
    photo = models.ImageField(
        verbose_name='Фото',
        upload_to='photos',
    )

    class Meta:
        verbose_name='Педагог'
        verbose_name_plural='Педагоги'
