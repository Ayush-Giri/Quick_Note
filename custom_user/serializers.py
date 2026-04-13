from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator


User = get_user_model()

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )

    def validate(self, obj):
        if obj.get("password") != obj.get("confirm_password"):
            raise serializers.ValidationError("passwords do not match")
        return obj
    

    def to_internal_value(self, data):
        # to internal value gets dict
        data = data.copy()
        if data.get('username'):
            data['username'] = data["username"].strip()
        if data.get('email'):
            data['email'] = data['email'].strip()
        return super().to_internal_value(data)
    
    def create(self, validated_data):
        validated_data = validated_data.copy()
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)

    



  