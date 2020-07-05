from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework import generics
from login.userserlizer import UserSerializerr
# Create your views here.
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def loginuser(request):
	username=request.data.get('username')
	password=request.data.get('password')
	if username is None and password is None:
		return Response({'error':'Please Provide Both Username and Passowrd'},status=HTTP_400_BAD_REQUEST)
	user=authenticate(username=username,password=password) 
	if not user:
		return Response({'error':'Please provide Correct Credentials'},status=HTTP_404_NOT_FOUND)
	token,key=Token.objects.get_or_create(user=user)
	return Response({'token':token.key},status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def sayHello(request):
	return Response('Hello Motherfucker...')


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerr
    permission_classes = (AllowAny, )


