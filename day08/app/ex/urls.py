from django.urls import path

from .views import Index


app_name = 'ex'
urlpatterns = [
    path('', Index.as_view(), name='index'),
]
