from rest_framework import views
from rest_framework.response import Response
from rest_framework.exceptions import APIException, NotFound
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from .models import MyUser
from .serializers import MyUserSerializer
from my_auth.utils import get_access_token, get_refresh_token

class MyUserRegisterView(views.APIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    
    def get(self, request):
        return Response({"msg": "this is get"})
    
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        try:
            new_user = MyUser.objects.create(email=email, password=password)
        except IntegrityError as e:
            print(e)
            raise NotFound("User with this email already exists")
            
        return Response({"id": new_user.id, "email": new_user.email})

class MyUserLoginView(views.APIView):
    serializer_class = MyUserSerializer
    
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        try:
            MyUser.objects.get(email=email, password=password)
        except ObjectDoesNotExist:
            raise NotFound("Wrong email or password")
        return Response({"access_token": get_access_token({"email": email}),
                         "refresh_token": get_refresh_token()})

# class TokenRefresh(views.APIView):
#     def post(self, request):
#         if db.refresh_token == request.data["refresh_token"]:
#             return Response({"access_token": get_access_token({"email": email}),
#                          "refresh_token": get_refresh_token()})