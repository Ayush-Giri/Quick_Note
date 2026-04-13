from django.shortcuts import render
from rest_framework.views import APIView
from custom_user.models import CustomUser
from custom_user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CreateUser(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "user created successfully"
                 },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

