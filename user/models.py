from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Child(models.Model):
    phone_number_regex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    education_orientation = [
        ('OBJ','Основы безопасности жизнедеятельности'),
        ('NPV',"Нравствено-патриотическое воспитание"),
        ('KET',"Культурно-этические нормы"),
        ('VFK',"Воспитание финансовой культуры"),
        ('EV',"Экологическое воспитание"),
        ('IR',"Индивидуальное развитие"),
        ('RR',"Развитие речи"),
        ('MO',"Методика общения"),
        ('HER',"Художествено-эстетическое развитие"),
        ('MRV',"Музыкально-ритмическое воспитание"),
        ('FV',"Физическое воспитание"),
        ('RKRT',"Развитие конструирования и ручного труда"),
    ]
    specialist_services = [
        ('LD',"Логопед-дефектолог"),
        ('S',"Сурдопедагог (Нарушение слуха)"),
        ('T',"Тифлопедагог (Нарушение зрения)"),
    ]

    full_name = models.CharField(
        verbose_name='Ф.И.О. ребёнка', 
        max_length=50,
    )
    bdd = models.DateField(verbose_name='Дата рождения')
    parent_full_name = models.CharField(
        verbose_name='Ф.И.О. родителя(ей)', 
        max_length=50,
    )
    phone_number = models.CharField(
        verbose_name='Номер телефона родителя/опекуна', 
        max_length=14,
        validators = [phone_number_regex],
    )
    art_club = models.BooleanField(verbose_name="Юный художник (Рисование)")
    dance_club = models.BooleanField(verbose_name="Танцуем вместе (Танцы)")
    music = models.BooleanField(verbose_name="Весёлые нотки (Музыкальный кружок)")
    physical_culture_club = models.BooleanField(verbose_name="Спортивные ребята (Физкультурный кружок)")
    needlework_club = models.BooleanField("Волшебные ручки (Рукоделие)")
    robotics = models.BooleanField(verbose_name="Ротоботехника")
    foreign_languages = models.BooleanField(verbose_name="Английский язык")
    orientation_of_education = models.CharField(
        verbose_name='Направленость обучения',
        max_length=4,
        choices=education_orientation,
    )
    specialist_service = models.CharField(
        verbose_name='Услуги специалиста',
        max_length=4,
        choices=specialist_services,
    )
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="Педагог")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name='Ребёнок'
        verbose_name_plural='Дети'