from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms
from . import models

# 1. Home Page -> Now requires Login
# 添加 LoginRequiredMixin，如果用户未登录，访问此页面会自动跳转到 settings.LOGIN_URL (默认是 /accounts/login/，我们需要在 urls.py 改成 /login/)
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'web_book1/index.html'

# 2. Registration Page
class UserCreateView(CreateView):
    # 使用 forms.py 中定义的包含密码处理的 CustomUserCreationForm
    form_class = forms.CustomUserCreationForm
    template_name = 'web_book1/form_page.html'
    
    # 注册成功后跳转到登录页面
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        return super().form_valid(form)

# 3. User List Page (Kept as is)
class UserListView(LoginRequiredMixin, ListView): # 可选：也可以给列表页加锁
    model = models.User
    template_name = 'web_book1/show_all_users.html'
    context_object_name = 'users_record'

# 4. New: Login View
class UserLoginView(LoginView):
    template_name = 'web_book1/login.html'
    # 登录成功后跳转到主页 (也可以在 settings.py 设置 LOGIN_REDIRECT_URL)
    next_page = 'index'

# 5. New: Logout View
class UserLogoutView(LogoutView):
    # 登出后跳转到登录页或主页
    next_page = 'login'