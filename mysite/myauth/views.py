from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


def logout_view(request):
    logout(request)
    return redirect('myauth:login')

# Պետք է ստուգել
# class MyLogoutView(LogoutView):
#     next_page = reverse_lazy('myauth:login')


class AboutMeView(TemplateView):
    template_name = 'myauth/about-me.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response
    