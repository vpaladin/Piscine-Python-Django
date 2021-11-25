from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.expressions import Case
from django.db.models.fields import DateField, DateTimeField, TextField
from django.db.models.fields.related import ManyToManyField
from django.utils import timezone


class Tip(models.Model):
    text = TextField(blank=True)
    user = models.ForeignKey(User, related_name='tips', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_dis_likes(self):
        return self.dislikes.users.count()
    
    def __str__(self):
        return str(self.text)[:30]


class Like(models.Model):
    tip = models.OneToOneField(Tip, related_name='likes', on_delete=CASCADE)
    users = models.ManyToManyField(User, related_name='appreciate')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return (self.tip.tips)[:30]


class Dislike(models.Model):
    tip = models.OneToOneField(Tip, related_name='dislikes', on_delete=CASCADE)
    users = models.ManyToManyField(User, related_name='disregard')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return (self.tip.tips)[:30]