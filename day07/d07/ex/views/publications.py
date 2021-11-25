from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Article


class Publications(LoginRequiredMixin, ListView):
    model = Article
    template_name = "publications.html"
    context_object_name = 'publications'
    allow_empty = False

    def get_queryset(self):
        queryset = Article.objects.filter(author= self.request.user)
        return queryset
