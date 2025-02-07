from rest_framework import views
from .models import MyUser
from .serializers import MyUserSerializer
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework.exceptions import APIException, NotFound

class MyUserView(views.APIView):
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