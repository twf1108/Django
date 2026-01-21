from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms
from . import models

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'web_book1/index.html'

class UserCreateView(CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = 'web_book1/form_page.html'
    
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        return super().form_valid(form)

class UserListView(LoginRequiredMixin, ListView): 
    model = models.User
    template_name = 'web_book1/show_all_users.html'
    context_object_name = 'users_record'

class UserLoginView(LoginView):
    template_name = 'web_book1/login.html'
    next_page = 'index'

class UserLogoutView(LogoutView):
    next_page = 'login'