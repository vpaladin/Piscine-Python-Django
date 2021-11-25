from django.shortcuts import render

# Create your views here.

def post_django(req):
    return render(req, 'ex01/django.html', {})

def post_display(req):
    return render(req, 'ex01/display.html', {})

def post_templates(req):
    return render(req, 'ex01/templates.html', {})
