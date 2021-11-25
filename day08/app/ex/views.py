from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView
from django.contrib import messages

from .models import Image
from .forms import FormImage


class Index(ListView, FormView):
    template_name = 'index.html'
    success_url = reverse_lazy('ex:index')
    model = Image
    form_class = FormImage
    context_object_name = 'images_list'
    queryset = model.objects.all()

    def form_valid(self, form: FormImage):
        form.save()
        messages.success(self.request, "Success")
        return super().form_valid(form)

    def form_invalid(self, form: FormImage):
        messages.error(self.request, 'Not success')
        return super().form_invalid(form)
