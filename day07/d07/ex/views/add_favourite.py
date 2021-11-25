from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from ..models import UserFavouriteArticle, Article


class AddFavourite(CreateView):
    model = UserFavouriteArticle
    fields = []
    success_url = reverse_lazy('favourite')

    def form_valid(self, form):
        pk = self.kwargs.get('pk', None)
        form.instance.user_id = self.request.user.id
        form.instance.author = self.request.user
        form.instance.article = get_object_or_404(Article, id=pk)
        messages.success(self.request, 'Новость была успешно добавлена в избранное!')
        return super().form_valid(form)