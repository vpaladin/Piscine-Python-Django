from django import forms
from .models import Tip

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ('text',)
        widgets = {
          'text': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }
        labels = {
            'text': False
        }
