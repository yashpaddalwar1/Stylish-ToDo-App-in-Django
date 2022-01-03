from django.contrib.auth import forms
from django.forms import ModelForm
from django.forms.fields import DateField
from django.forms.widgets import DateInput
from .models import Todo
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'deadline': DateInput(),
        }