from django.db import models
from django.db.models.fields import CharField


class Movies(models.Model):
    class Meta:
        db_table = "ex05_movies"
    title = models.CharField(max_length=64)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = CharField(max_length=32)
    producer = CharField(max_length=128)
    release_date = models.DateField()

    def __str__(self) -> str:
        return self.title
