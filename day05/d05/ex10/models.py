from django.db import models
from django.utils import timezone

# Create your models here.

class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    climate = models.TextField(null=True)
    diameter = models.IntegerField(null=True)
    orbital_period = models.IntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.IntegerField (null=True)
    surface_water = models.FloatField (null=True)
    terrain = models.TextField(null=True)
    created = models.DateTimeField(default=timezone.now, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.name

class People(models.Model):
    name = models.CharField(max_length=64)
    birth_year = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=32, null=True)
    eye_color = models.CharField(max_length=32, null=True)
    hair_color = models.CharField(max_length=32, null=True)
    height = models.IntegerField (null=True)
    mass = models.FloatField (null=True)
    homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE, max_length=64, null=True)
    created = models.DateTimeField(default=timezone.now, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.name

class Movies(models.Model):
    class Meta:
        db_table = "ex10_movies"
    title = models.CharField(max_length=64)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()
    created = models.DateTimeField(default=timezone.now, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    characters = models.ManyToManyField(People, related_name='films')
    
    def __str__(self) -> str:
        return self.title