from django import forms
from django.forms.fields import DateField
from django.forms.widgets import DateInput, Select
from .models import People
import datetime


def round_tuple():
    round_list = People.objects.all().values('gender').distinct()
    round_list = [(x['gender'], x['gender']) for x in round_list]
    return round_list

class Form(forms.Form):
    min_release_data = forms.DateField(widget=DateInput(attrs={'type': 'date', 'name': 'Минимальная дата релиза'}), initial=format(datetime.date.today()))
    max_release_data = forms.DateField(widget=DateInput(attrs={'type': 'date'}), initial=format(datetime.date.today()))
    diameter_greater_than = forms.IntegerField(initial=0)
    gender = forms.CharField(widget=forms.Select(choices=round_tuple()))
