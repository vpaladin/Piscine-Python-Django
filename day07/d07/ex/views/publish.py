from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import DatabaseError
from django.shortcuts import redirect
from ..models import Article


class Publish(LoginRequiredMixin, CreateView):
    template_name = 'publish.html'
    model = Article
    fields = ['title', 'synopsis', 'content']

    def form_valid(self, form):
        form.instance.CustomUser = self.request.user
        form.instance.author = self.request.user
        messages.success(self.request, 'Success published!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid data!')
        return super().form_invalid(form)

