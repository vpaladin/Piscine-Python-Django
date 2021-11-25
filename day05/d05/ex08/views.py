import psycopg2
from django.shortcuts import render, redirect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error
from django.conf import settings

def init_people_and_planets():
    planets = """CREATE TABLE ex08_planets(
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(64) UNIQUE NOT NULL,
                            climate TEXT,
                            diameter INTEGER,     
                            orbital_period INTEGER,
                            population BIGINT,
                            rotation_period INTEGER,
                            surface_water REAL,
                            terrain VARCHAR(128)
                            );"""
    people = """CREATE TABLE ex08_people(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(64) UNIQUE NOT NULL,
                        birth_year VARCHAR(32),     
                        gender VARCHAR(32),     
                        eye_color VARCHAR(32),
                        hair_color VARCHAR(32),
                        height INTEGER,
                        mass REAL,
                        homeworld VARCHAR(128),
                        FOREIGN KEY (homeworld) REFERENCES ex08_planets (name)
                        );"""
    return (people, planets)

def init_data():
    planets_path = settings.DATA_PLANETS  
    people_path = settings.DATA_PEOPLES
    planets_col= ('name', 'climate', 'diameter', 'orbital_period', 
                'population', 'rotation_period', 'surface_water',
                'terrain')
    people_col = ('name', 'birth_year', 'gender', 'eye_color', 
                'hair_color', 'height', 'mass', 'homeworld')
    return planets_path, people_path, planets_col, people_col

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
                cursor.execute("DROP TABLE ex08_people;")
                cursor.execute("DROP TABLE ex08_planets;")
            except (Exception, Error) as error:
                print(error)
            finally:
                if connect:
                    cursor.close()
                    connect.close()
    return render(request, 'ex08/index.html')

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
        people, planets = init_people_and_planets()
        try:
            cursor.execute(planets)
            res.append("OK")
        except (Exception, Error) as error:
            res.append(error)
        try:
            cursor.execute(people)
            res.append("OK")
        except (Exception, Error) as error:
            res.append(error)
    except (Exception, Error) as error:
        print(error)
    finally:
        if connect:
            cursor.close()
            connect.close()
    return render(request, 'ex08/index.html', {"res": res})

def display(request):
    res = []
    peoples = []
    try:
        connect = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        with connect.cursor() as curs:
            curs.execute("""SELECT PE.name as name, homeworld, climate
                        FROM ex08_people as PE, ex08_planets as PL 
                        WHERE PE.id = PL.id
                        ORDER BY name ASC;""")
            peoples = curs.fetchall()
    except (Exception, Error) as error:
        print(error)
        res.append(error)
    finally:
        if connect:
            connect.close()
    return (render(request, 'ex08/display.html', {"peoples":peoples, "res": res}))


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
        with connect.cursor() as curs:
            planets_path, people_path, planets_col, people_col= init_data()
            try:
                curs.copy_from(file=open(planets_path), table='ex08_planets', columns=planets_col, sep='\t', null="NULL")
                res.append("OK")
            except (Exception, Error) as error:
                res.append(error)
            try:
                curs.copy_from(file=open(people_path), table='ex08_people', columns=people_col, sep='\t', null="NULL")
                res.append("OK")
            except (Exception, Error) as error:
                res.append(error)
    except (Exception, Error) as error:
        print(error)
        res.append(str(error))
    finally:
        if connect:
            connect.close()
    return render(request, 'ex08/index.html', {"res": res})
    