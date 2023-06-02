from django import forms


class AnswerForm(forms.Form):
    email = forms.EmailField()
    answer_text = forms.CharField(
        label='Текст ответа',
        widget=forms.Textarea(
            attrs={
                'cols': 60,
                'rows': 10,
            }
        ),
    )
