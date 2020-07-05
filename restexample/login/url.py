from django.contrib import admin
from django.urls import path
from  login import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('api/login',obtain_auth_token),
    path('api/hello',views.sayHello),
    path('api/register', views.UserCreate.as_view())
]
