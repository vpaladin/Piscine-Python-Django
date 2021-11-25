from django.urls import path
from .views import home, articles, login, publications, detail, favourite, register, publish, add_favourite

urlpatterns = [
    path("", home.Home.as_view(), name="home"),
    path("articles/", articles.Articles.as_view(), name="articles"),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', login.Logout.as_view(), name='logout'),
    path('publications/', publications.Publications.as_view(), name='publications'),
    path('articles/<int:pk>', detail.Detail.as_view(), name='articles_detail'),
    path('favourite/', favourite.Favourite.as_view(), name='favourite'),
    path('register/', register.Register.as_view(), name='register'),
    path('publish/', publish.Publish.as_view(), name='publish'),
    path('articles/<int:pk>/add_favourite', add_favourite.AddFavourite.as_view(), name='add_favourite'),
]
