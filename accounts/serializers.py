from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions 

User = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        extra_kwargs = {"password" : {"write_only": True}}
        
    def validate(self, data):
        user = User(**data)
        password = data.get("password")
        
        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {"password": serializer_errors['non_field_errors']}
            )
        
        return data
        
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