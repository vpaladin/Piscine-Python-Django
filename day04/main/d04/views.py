from django.shortcuts import render


def index(request):
    return render(request, 'd04/base.html')