from rest_framework import views
from rest_framework.response import Response
from rest_framework.exceptions import APIException, NotFound
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from jwt.exceptions import ExpiredSignatureError

from .models import MyUser, RefreshToken
from .serializers import MyUserSerializer
from my_auth.utils import get_access_token, get_refresh_token, decode_access_token

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
            raise NotFound("User with this email already exists")
            
        return Response({"id": new_user.id, "email": new_user.email})

class MyUserLoginView(views.APIView):
    serializer_class = MyUserSerializer
    
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        try:
            user = MyUser.objects.get(email=email, password=password)
        except ObjectDoesNotExist:
            user = None
            raise NotFound("Wrong email or password")
        if user:
            refresh_token = get_refresh_token()
            token = RefreshToken(user=user, token = refresh_token)
            token.set_time()
            token.save()
        return Response({"access_token": get_access_token({"email": email}),
                         "refresh_token": refresh_token})

class MyUserRefreshView(views.APIView):
    def post(self, request):
        try:
            token = RefreshToken.objects.get(token=request.data["refresh_token"])
        except ObjectDoesNotExist:
            token = None
            raise NotFound("Wrong token")

        if token:
            email = token.user.email
            token.delete()
            refresh_token = get_refresh_token()
            new_refresh_token = RefreshToken(user=token.user, token=refresh_token)
            new_refresh_token.set_time()
            new_refresh_token.save()
            return Response({"access_token": get_access_token({"email": email}),
                         "refresh_token": refresh_token})   

class MyUserLogoutView(views.APIView):
    def post(self, request):
        try:
            token = RefreshToken.objects.get(token=request.data["refresh_token"])
        except:
            token = None
            raise NotFound("Wrong token")
        if token:
            token.delete()
            return Response({"success": "User logged out"})

class MyUserInformationView(views.APIView):
    def get(self, request):      # print(request.META["HTTP_AUTHORIZATION"])
        access_token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
        try:
            email = decode_access_token(access_token)["email"]
            user = MyUser.objects.get(email=email)
        except ExpiredSignatureError:
            user = None
            raise NotFound("Token expired")
        except ObjectDoesNotExist:
            user = None
            raise NotFound("Wrong token")
        if user:
            return Response({"id": user.id, "username": user.username, "email": user.email})
        else:
            return NotFound("Wrong token") 
    
    def put(self, request):
        access_token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
        try:
            email = decode_access_token(access_token)["email"]
        except ExpiredSignatureError:
            email=None
            raise NotFound("Token expired")
        if email:
            try:
                user = MyUser.objects.get(email=email)
            except ObjectDoesNotExist:
                user=None
                raise NotFound("Wrong token")
            if user:
                if request.data:
                    try:
                        user.update(username=request.data["username"], email=request.data["email"])
                    except Exception as e:
                        raise NotFound("User already exists")
            return Response({"data": request.data})