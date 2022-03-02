from django.contrib import admin
from django.urls import path, include

from accounts import views
app_name = 'accounts'
urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('register', views.user_register, name='user_register'),
]
