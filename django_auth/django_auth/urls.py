from django.urls import include, path
from rest_framework import routers
from my_auth.views import MyUserView

urlpatterns = [
    # path('', MyUserView.as_view()),
    path('register', MyUserView.as_view()),
]