import psycopg2
from django.shortcuts import render, redirect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error
from django.conf import settings
from . import forms

def init_dict():
    movies = [
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
    INSERT_DATA = """
        INSERT INTO ex06_movies
        (
            episode_nb,
            title,
            director,
            producer,
            release_date
        )
        VALUES
        (
            %s, %s, %s, %s, %s
        );"""
    return (movies, INSERT_DATA)

def index(request):
    if request.method == "POST":
        if 'create' in request.POST:
            return redirect("init/")
        elif 'display' in request.POST:
            return redirect("display/")
        elif 'remove' in request.POST:
            return redirect("remove/")
        elif 'populate' in request.POST:
            return redirect("populate/")
        elif 'update' in request.POST:
            return redirect("update/")
        elif 'delete' in request.POST: 
            try:
                connect = psycopg2.connect(
                    dbname=settings.DATABASES['default']['NAME'],
                    user=settings.DATABASES['default']['USER'],
                    password=settings.DATABASES['default']['PASSWORD'],
                    host=settings.DATABASES['default']['HOST'],
                    port=settings.DATABASES['default']['PORT'])
                connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cursor = connect.cursor()
                create_table = """DROP TABLE ex06_movies;"""
                cursor.execute(create_table);
            except (Exception, Error) as error:
                print(error)
            finally:
                if connect:
                    cursor.close()
                    connect.close()
    return render(request, 'ex06/index.html')

def init(request):
    res = []
    try:
        connect = psycopg2.connect(
                    dbname=settings.DATABASES['default']['NAME'],
                    user=settings.DATABASES['default']['USER'],
                    password=settings.DATABASES['default']['PASSWORD'],
                    host=settings.DATABASES['default']['HOST'],
                    port=settings.DATABASES['default']['PORT'])
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connect.cursor()
        create_table = """
                        CREATE TABLE ex06_movies
                        (title VARCHAR(64) NOT NULL,
                        episode_nb INT PRIMARY KEY NOT NULL,
                        open_crawl TEXT,     
                        director VARCHAR(32) NOT NULL,
                        producer VARCHAR(128) NOT NULL,
                        release_date  DATE NOT NULL,
                        created TIMESTAMP NOT NULL DEFAULT NOW(),
                        updated TIMESTAMP NOT NULL DEFAULT NOW()
                        );
                        
                        CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                        RETURNS TRIGGER AS $$
                        BEGIN
                        NEW.updated = now();
                        NEW.created = OLD.created;
                        RETURN NEW;
                        END;
                        $$ language 'plpgsql';
                        CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                        ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
                        update_changetimestamp_column();"""
        cursor.execute(create_table);
        res.append("OK")
    except (Exception, Error) as error:
        print(error)
        res.append(str(error))
    finally:
        if connect:
            cursor.close()
            connect.close()
    return render(request, 'ex06/index.html', {"res": res})

def display(request):
    res = []
    movies = []
    try:
        connect = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        with connect.cursor() as curs:
            curs.execute("SELECT * FROM ex06_movies;")
            movies = curs.fetchall()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        res.append(str(error))
    finally:
        if connect:
            connect.close()
    return (render(request, 'ex06/display.html', {"movies":movies, "res": res}))


def populate(request):
    res = []
    try:
        connect = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        movies, INSERT_DATA = init_dict()
        with connect.cursor() as curs:
            curs.execute("SET TIMEZONE='Europe/Moscow';");
            for movie in movies:
                try:
                    curs.execute(INSERT_DATA, [
                        movie['episode_nb'],
                        movie['title'],
                        movie['director'],
                        movie['producer'],
                        movie['release_date'],
                    ])
                    res.append("OK")
                except (Exception, Error) as error:
                    res.append(error)
    except (Exception, Error) as error:
        print(error)
        res.append(str(error))
    finally:
        if connect:
            connect.close()
    return render(request, 'ex06/index.html', {"res": res})
    
def remove(request):
    movies=[]
    try:
        connect = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'])
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with connect.cursor() as curs:
            if request.method == "POST":
                val = request.POST.get('remov_film')
                create_table = f"DELETE FROM ex06_movies WHERE title='{val}';"
                curs.execute(create_table);
            curs.execute("SELECT * FROM ex06_movies;")
            movies = curs.fetchall()
    except (Exception, Error) as error:
            print(error)
    finally:
        if connect:
            connect.close()
    return render(request, 'ex06/remove.html', {'movies': movies})

def update(request):
    movies=[]
    try:
        connect = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'])
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with connect.cursor() as curs:
            curs.execute("SET TIMEZONE='Europe/Moscow';");
            if request.method == "POST":
                val = request.POST.get('update_film')
                open_crawl = request.POST.get('open_crawl')
                update_table = f"UPDATE ex06_movies SET open_crawl='{open_crawl}' WHERE title='{val}';"
                curs.execute(update_table);
            curs.execute("SELECT * FROM ex06_movies;")
            movies = curs.fetchall()
    except (Exception, Error) as error:
            print(error)
    finally:
        if connect:
            connect.close()
    return render(request, 'ex06/update.html', {'movies': movies, "form": forms.OpenCrawl() })