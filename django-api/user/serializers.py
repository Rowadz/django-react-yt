from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
)
from .models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)

        token['name'] = user.username
        token['email'] = user.email
        token['user_id'] = user.id
        return token


class RegisterSerializer(ModelSerializer):
    password_confirmation = CharField(required=False)
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = CharField(
        required=True,
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username',
            'password', 'password_confirmation',
            'email',
        )

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise ValidationError({'error_message': 'PAsswords do not match'})
        return data

    def create(self, validated_data):
        user: User = User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )

        user.set_password(validated_data.get('password'))
        user.save()

        return user
