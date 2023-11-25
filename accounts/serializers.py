from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        extra_kwargs = {"password" : {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data["email"],
            username = validated_data["username"],
            password = validated_data["password"],
        )
        user.generate_confirmation_token()
        return user
    
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)