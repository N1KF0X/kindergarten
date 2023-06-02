from django import forms
from application import models

class SendQuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['full_name', 'email', 'phone_number', 'text']
        #widgets = 

class SendTeacherAppForm(forms.ModelForm):
    class Meta:
        model = models.TeacherApplication
        fields = ['full_name', 'email', 'phone_number', 'education', 'specialization', 'experience', 'about_me']


class SendChildAppForm(forms.ModelForm):
    class Meta:
        model = models.ChildApplication
        fields = '__all__'
