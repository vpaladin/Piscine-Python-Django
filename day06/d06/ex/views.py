from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import FormView, View
from django.contrib.auth.forms import UserCreationForm
from .models import Tip, Like, Dislike
from .forms import TipForm


def get_rep(user):
    tips = user.tips.all()
    count_likes = 0
    count_dislike = 0
    for tip in tips:
        try:
            count_likes += tip.get_total_likes() * 5
        except:
            pass
    for tip in tips:
        try:
            count_dislike += tip.get_total_dis_likes() * 2
        except:
            pass
    return(count_likes - count_dislike)

class Index(View):
    template_name = 'index.html'

    def get(self, request):

        list_tips= Tip.objects.order_by('-updated_at')
        form = TipForm
        context = {'list_tips':list_tips, 'form':form }
        if request.user.is_authenticated:
            print(request.user.tips.all()[0].likes.users.count())
            user = request.user
            context['rep'] = get_rep(user)
        return render(request, self.template_name, context)

    def post(self, request):
        form = TipForm(request.POST)
        if form.is_valid():
            tip_form = form.save(commit=False)
            tip_form.user = request.user
            tip_form.save()
            messages.success(request, 'Your life tip successfully addedd')
        return redirect(reverse('index'))

    
class SignUp(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')

    def get(self, request):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'You already logined')
            return redirect('index')
        return super().get(request)

    def form_valid(self, form: UserCreationForm):
        user= form.save()
        login(self.request, user)
        messages.success(self.request, "Registration successful.")
        return super().form_valid(form)
    
    def form_invalid(self, form: UserCreationForm):
        messages.error(self.request, "Unsuccessful registration. Invalid information.")
        return super().form_invalid(form)

# class Login(FormView):
#     template_name = 'ex/login.html'
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('index')
    
#     def get(self, request):
#         if self.request.user.is_authenticated:
#             messages.error("Ты уже в вошел")
#             return redirect(index)
    
#     def form_valid(self, form: AuthenticationForm):
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(self.request,username=username, password=password)
#         if user is None:
#             messages.error(self.request, "Invalid login or password")
#             return
#         login(self.request, user)
#         messages.info(self.request, "Welcome to our site (^ ^)!")
#         return super().form_valid(form)
    
#     def form_invalid(self, form: AuthenticationForm):
#         return super().form_invalid(form)

class Login(LoginView):
    template_name = "login.html"
    succes_url = reverse_lazy('index')

class Logout(LogoutView):
    next_page = reverse_lazy('index')

class UpdateCommentVote(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):

        tip_id = self.kwargs.get('tip_id', None)
        opinion = self.kwargs.get('opinion', None)
        tip = get_object_or_404(Tip, id=tip_id)

        if opinion.lower() == 'delete':
            if request.user == tip.user or request.user.is_superuser == True:
                tip.delete()
                messages.success(self.request,"Ты успешно удалил совет!")
            else:
                messages.error(self.request,"Ты не имеешь на это права!")
            return redirect(reverse('index'))
        try:
            tip.dislikes
        except Tip.dislikes.RelatedObjectDoesNotExist as identifier:
            Dislike.objects.create(tip=tip)
        try:
            tip.likes
        except Tip.likes.RelatedObjectDoesNotExist as identifier:
            Like.objects.create(tip=tip)
        if opinion.lower() == 'like':
            if request.user in tip.likes.users.all():
                tip.likes.users.remove(request.user)
            else:    
                tip.likes.users.add(request.user)
                tip.dislikes.users.remove(request.user)
        elif opinion.lower() == 'dislike':
            if request.user == tip.user or get_rep(request.user) >= 15 or request.user.is_superuser == True:
                if request.user in tip.dislikes.users.all():
                    tip.dislikes.users.remove(request.user)
                else:
                    tip.dislikes.users.add(request.user)
                    tip.likes.users.remove(request.user)
            else:    
                messages.error(self.request,"Повысь свою репутацию!")
        return redirect(reverse('index'))
