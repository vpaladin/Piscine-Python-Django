from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path("login/", views.Login.as_view(), name='login'),
    path("logout/", views.Logout.as_view(), name='logout'),
    path("registration/", views.SignUp.as_view(), name='register'),
    path('<int:tip_id>/<str:opinion>', views.UpdateCommentVote.as_view(), name='grade'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/favicon.ico')),
]
