import psycopg2
from django.shortcuts import render, redirect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error
from django.conf import settings

def index(request):
    if request.method == "POST":
        if 'create' in request.POST:
            return redirect("init/")
        elif 'display' in request.POST:
            return redirect("display/")
        elif 'populate' in request.POST:
            return redirect("populate/")
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
                create_table = """DROP TABLE ex02_movies;"""
                cursor.execute(create_table);
            except (Exception, Error) as error:
                print("Ошибка при работе с PostgreSQL", error)
            finally:
                if connect:
                    cursor.close()
                    connect.close()
    return render(request, 'ex02/index.html')

def init(request):
    n = True
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
        create_table = """CREATE TABLE ex02_movies
                          (title VARCHAR(64) NOT NULL,
                          episode_nb INT PRIMARY KEY NOT NULL,
                          open_crawl TEXT,     
                          director VARCHAR(32) NOT NULL,
                          producer VARCHAR(128) NOT NULL,
                          release_date  DATE NOT NULL);"""
        cursor.execute(create_table);
    except (Exception, Error) as error:
        n = False
        print("Ошибка при работе с PostgreSQL", error)
        res = "Ошибка при работе с PostgreSQL" + str(error)
    finally:
        if connect:
            cursor.close()
            connect.close()
            print("Соединение с PostgreSQL закрыто")
    return render(request, 'ex02/index.html', {"n":n, "res": res})

def display(request):
    res = []
    n = True
    movies = []
    try:
        connect = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        SELECT_TABEL = f"""
            SELECT * FROM ex02_movies;"""
        with connect.cursor() as curs:
            curs.execute(SELECT_TABEL)
            movies = curs.fetchall()
    except (Exception, Error) as error:
        n = False
        print("Ошибка при работе с PostgreSQL", error)
        res = "Ошибка при работе с PostgreSQL" + str(error)
    finally:
        if connect:
            connect.close()
    return (render(request, 'ex02/display.html', {"movies":movies, "res": res, "n":n}))


def populate(request):
    n = True
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
        INSERT INTO ex02_movies
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
        with connect.cursor() as curs:
            for movie in movies:
                try:
                    curs.execute(INSERT_DATA, [
                        movie['episode_nb'],
                        movie['title'],
                        movie['director'],
                        movie['producer'],
                        movie['release_date'],
                    ])
                except (Exception, Error) as error:
                    n = False
                    print("Ошибка при работе с PostgreSQL", error)
                    res = "Ошибка при работе с PostgreSQL " + str(error)
    except (Exception, Error) as error:
        n = False
        print("Ошибка при работе с PostgreSQL", error)
        res = "Ошибка при работе с PostgreSQL" + str(error)
    finally:
        if connect:
            connect.close()
    return render(request, 'ex02/index.html', {"n":n, "res": res})
    
