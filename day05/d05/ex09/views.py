from django.shortcuts import render, redirect
from .models import Planets, People


def index(request):
    if request.method == "POST":
        if 'display' in request.POST:
            return redirect("display/")
        elif 'delete' in request.POST:
            res = []
            planets = Planets.objects.all()
            if planets:
                for planet in planets:
                    name = planet.name
                    try:
                        if planet not in planets:
                            raise Exception()
                        planet.delete()
                        res.append(f"OK. {name} удален :)")
                    except:
                        res.append(f"KO. {name} не существует :(")
            peoples = People.objects.all()
            if peoples:
                for human in peoples:
                    name = human.name
                    try:
                        if human not in peoples:
                            raise Exception()
                        human.delete()
                        res.append(f"OK. {name} удален :)")
                    except:
                        res.append(f"KO. {name} не существует :(")
            return render(request, "ex09/index.html", {"res": res})
    return render(request, 'ex09/index.html')

def display(req):
    people = People.objects.filter(homeworld__climate__contains='windy').order_by('name')
    return render(req, "ex09/display.html", {"people" : people })