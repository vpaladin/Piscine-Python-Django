import psycopg2
from django.shortcuts import render
from django.shortcuts import redirect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error


def index(request):
    if request.method == "POST":
        if 'create' in request.POST:
            return redirect("init/")
        elif 'delete' in request.POST: 
            try:
                connect = psycopg2.connect(user='djangouser',
                                            password='secret',
                                            host="127.0.0.1",
                                            port="5432",
                                            database='djangotraining')
                connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                cursor = connect.cursor()
                create_table = """DROP TABLE ex00_movies;"""
                cursor.execute(create_table);
            except (Exception, Error) as error:
                print("Ошибка при работе с PostgreSQL", error)
            finally:
                if connect:
                    cursor.close()
                    connect.close()
                print("Соединение с PostgreSQL закрыто")
    return render(request, 'ex00/index.html')

def init(request):
    n = True
    res = []
    try:
        connect = psycopg2.connect(user='djangouser',
                                    password='secret',
                                    host="127.0.0.1",
                                    port="5432",
                                    database='djangotraining')
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connect.cursor()
        create_table = """CREATE TABLE ex00_movies
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
    return (render(request, 'ex00/index.html', {"n":n, "res": res}))    

