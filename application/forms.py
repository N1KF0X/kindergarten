from django import forms
from application import models

class SendQuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['full_name', 'email', 'phone_number', 'text']


class SendTeacherAppForm(forms.ModelForm):
    class Meta:
        model = models.TeacherApplication
        fields = [
            'full_name', 
            'email', 
            'phone_number',
            'education', 
            'specialization',
            'experience', 
            'about_me',
        ]


class SendAdaptiveAppForm(forms.ModelForm):
    class Meta:
        model = models.AdaptiveApplication
        fields = [
            'full_name', 
            'email', 
            'phone_number', 
            'child_full_name',
        ]


class SendChildAppForm(forms.ModelForm):
    class Meta:
        model = models.ChildApplication
        fields = [
            'full_name', 
            'email', 
            'phone_number', 
            'child_full_name', 
            'orientation_of_education', 
            'art_club',
            'dance_club',
            'music',
            'physical_culture_club',
            'needlework_club',
            'robotics',
            'foreign_languages',
            'specialist_service',
        ]
