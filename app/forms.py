from django import forms
from django.core import validators

class TopicForm(forms.Form):
    name=forms.CharField(max_length=20,validators=[validators.MinLengthValidator(5)])
    age=forms.IntegerField(validators=[validators.MinValueValidator(18)])
    mobileno=forms.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
