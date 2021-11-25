from django.db import models
from django.conf import settings


class Image(models.Model):
    title = models.CharField(max_length=64, )
    image = models.ImageField()

    class Meta:
        db_table = 'Images'
        ordering = ['-id']
