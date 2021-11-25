from django import forms

class LogHistory(forms.Form):
    history_log = forms.CharField(label='History log')
