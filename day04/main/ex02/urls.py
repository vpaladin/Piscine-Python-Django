from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_history, name="index")
]