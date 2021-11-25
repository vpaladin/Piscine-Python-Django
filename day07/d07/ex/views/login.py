from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class Login(LoginView):
    template_name = "login.html"
    succes_url = reverse_lazy('home')

class Logout(LogoutView):
    next_page = reverse_lazy('home')