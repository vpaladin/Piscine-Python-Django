from django import forms

class OpenCrawl(forms.Form):
    open_crawl = forms.CharField(widget=forms.Textarea(), label="")
