from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from auth.serializers import UserSerializer
from django.contrib.auth.models import User
import jwt
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def get_custom_response(success=False, message='something went wrong', data=None, status=400):
    
    response = {
        'success': success,
        'message': message,
        'data': data
    }
    return Response(response, status=status)



class Registration(APIView):
    """
    Registration or create user CBV

    """
   
    def post(self,request):
        try:
        
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = get_custom_response(success=True,message="Sucessful",data=serializer.data,status=200)
                return response
            else:
                error = get_custom_response(data=serializer.errors)
                return error

        except Exception as e:
            print(e)
            error = get_custom_response()
            return error

class LoginView(APIView):
    """
    Login CBV

    """

    def post(self,request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            if username != None and password != None:
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    payload = {
                        'username': user.username,
                        'password': user.password,
                    }
                    key = 'core'
                    token = jwt.encode(payload, key, algorithm='HS256')
                    login(request,user)
                    response = get_custom_response(success=True,message="Sucessful",data=token,status=200)
                    return response
                else:
                    error = get_custom_response()
                    return error
                    
            else:
                error = get_custom_response(messaage='Please provide valid credentials!')
                return error
        except Exception as e:
            error = get_custom_response()
            return error




