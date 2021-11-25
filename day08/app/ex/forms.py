from django.forms import ModelForm

from .models import Image


class FormImage(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
