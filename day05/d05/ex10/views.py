from django.shortcuts import render
from .models import People
from .forms import Form

def index(request):
    # films = []
    people = []
    if request.method == "POST":
        form = Form(request.POST or None)
        print(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get('min_release_data')
            end_date = form.cleaned_data.get('max_release_data')
            diameter = form.cleaned_data.get('diameter_greater_than')
            sex = form.cleaned_data.get('gender')
            people = People.objects.filter(gender=sex, homeworld__diameter__gt = diameter,
                                            films__release_date__range=[start_date, end_date]).values(
                                                "name", "gender", "films__title", "homeworld__name",
                                                "homeworld__diameter")
            # people = People.objects.filter(gender=sex, homeworld__diameter__gt = diameter) #нахожу людей
            # heroes = {}
            # for x in people:
            #     heroes[str(x)] = x.films.filter(release_date__range=[start_date, end_date])
            #     heroes ={k:v for k, v in heroes.items() if v}
            # print(people2)
            # films = []
            # for k,v in heroes.items():
            #     for movie in v:
            #         hero = movie.characters.filter(name=k).get()
            #         films.append([hero, hero.gender, movie, hero.homeworld, hero.homeworld.diameter])
    return render(request, 'ex10/index.html', {'form' : Form, "people": people })

"""Имя персонажа• Их пол• Название фильма• Название родного мира• Диаметр родного мира"""