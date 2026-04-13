from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from rest_framework import permissions

# Create your views here.


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        queryset = UserProfile.objects.filter(user=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

    


