from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login

class Register(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def get(self, request):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'You already logined')
            return redirect('index')
        return super().get(request)

    def form_valid(self, form: UserCreationForm):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Registration successful.")
        return super().form_valid(form)

    def form_invalid(self, form: UserCreationForm):
        messages.error(self.request, "Unsuccessful registration. Invalid information.")
        return super().form_invalid(form)
