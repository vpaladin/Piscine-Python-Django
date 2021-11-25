from django.forms import ModelForm,TextInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import UserFavouriteArticle

class FavouriteForm(ModelForm):
    class Meta:
        model = UserFavouriteArticle
        fields = []


# class LoginForm(AuthenticationForm):
#     username = UsernameField(widget=TextInput(attrs=))