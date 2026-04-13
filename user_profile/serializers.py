from rest_framework.serializers import ModelSerializer
from user_profile.models import UserProfile

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'profile_image'
        ]