from .models import MyUser
from rest_framework import serializers


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'password']