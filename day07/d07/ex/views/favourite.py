from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import UserFavouriteArticle

class Favourite(LoginRequiredMixin, ListView):
    template_name = 'favourites.html'
    model = UserFavouriteArticle
    context_object_name = 'favorite_list'
    allow_empty = False

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset