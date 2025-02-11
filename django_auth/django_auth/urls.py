from django.urls import include, path
from rest_framework import routers
from my_auth.views import MyUserRegisterView, MyUserLoginView

urlpatterns = [
    # path('', MyUserView.as_view()),
    path('register', MyUserRegisterView.as_view()),
    path('login', MyUserLoginView.as_view()),
]