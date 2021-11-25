from django.shortcuts import render

# Create your views here.

def index(req):
    step = 100 / 50
    steps = [f"{(int(step * x))}" for x in range(50)]
    return render(req, 'ex03/content.html', {'steps' : steps})