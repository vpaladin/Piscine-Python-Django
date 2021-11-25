from django.urls import path
from . import views

urlpatterns = [
    path("django", views.post_django, name="post_django"),
    path("display", views.post_display, name="post_display"),
    path("templates", views.post_templates, name="post_templates"),
]
