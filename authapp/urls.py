from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import render
from . import views
from django.contrib.auth import views as auth_views

app_name= 'authapp'
urlpatterns = [
    path('', views.AccountHomePageView.as_view(), name='home'),
    path('profile', views.profilePicture, name='profileUpload'),
    path('user-login', auth_views.LoginView.as_view(template_name = 'authTemplates/user-login.html'), name='login'),
    path('profile/', views.AccountHomePageView.as_view(), name='profile'),
    path('logout', auth_views.LogoutView.as_view(template_name= 'authTemplates/logout.html'), name= 'logout'),
    path('signup', views.UserSignUpView.as_view(), name='signup'),
    path('password-change', auth_views.PasswordChangeView.as_view(template_name = 'authTemplates/password_change.html'), name='change_password'),
    re_path('password_reset', auth_views.PasswordResetView.as_view(template_name = 'authTemplates/registration/forgot_password.html'), name='reset_password'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name = 'authTemplates/registration/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name = 'authTemplates/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name = 'authTemplates/registration/password_reset_complete.html'), name='password_reset_complete'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)