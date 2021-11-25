from django.shortcuts import render

# Create your views here.

def markdown(request):
    return render(request, 'ex00/index.html', {})
