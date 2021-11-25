from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Movies
from . import forms

def index(request):
    if request.method == "POST":
        if 'display' in request.POST:
            return redirect("display/")
        elif 'populate' in request.POST:
            return redirect("populate/")
        elif 'update' in request.POST:
            return redirect("update/")
        elif 'remove' in request.POST:
            movies = Movies.objects.all()
            return redirect("remove/", {'movies': movies})
        elif 'delete' in request.POST:
            res = []
            movies = Movies.objects.all()
            if movies:
                for movie in movies:
                    title = movie.title
                    try:
                        if movie not in movies:
                            raise Exception()
                        movie.delete()
                        res.append(f"OK. {title} удален :)")
                    except:
                        res.append(f"KO. {title} не существует :(")
            else:
                res.append("KO. Ни одного фильма не найдено в базе :(")
            return render(request, "ex07/res.html", {"res": res})
    return render(request, 'ex07/index.html')

def display(request):
    movies = Movies.objects.all()
    return (render(request, 'ex07/display.html', {"movies": movies }))


def remove(request):
    movies = Movies.objects.all()
    if request.method == "POST":
        value = request.POST.get("remov_film")
        moveie = Movies.objects.get(title=value)
        moveie.delete()
        movies = Movies.objects.all()
    return render(request, 'ex07/remove.html', {'movies': movies})

def update(request):
    movies = Movies.objects.all()
    movies_title = [movie.title for movie in movies]
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("title")
        value = request.POST.get("opening_crawl")
        movie = Movies.objects.get(title=name)
        movie.opening_crawl = value
        movie.save()
    return render(request, 'ex07/update.html', {'movies': movies, "form": forms.OpenCrawl(movies_title)})
    

def populate(request):
    res = []
    movies = []
    films = [
            {
                "episode_nb": 1,
                "title": "The Phantom Menace",
                "director": "George Lucas",
                "producer": "Rick McCallum",
                "release_date": "1999-05-19"
            },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        }
    ]
    for film in films:
        movies.append(Movies(
            title=film["title"], episode_nb= film["episode_nb"],
            director=film["director"], producer=film["producer"],
            release_date=film["release_date"]))
    for movie in movies:
        title=movie.title
        try:
            if movie in Movies.objects.all():
                raise Exception()
            movie.save()
            res.append(f"OK. {title} добавлен :)")
        except:
            res.append(f"KO. {title} уже в базе :)")
    return render(request, 'ex07/res.html', {"res": res})
    
