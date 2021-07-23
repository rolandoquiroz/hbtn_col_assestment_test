from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.validators import is_alphanumeric
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        max_length=255,
        validators=[
            validate_email,
            UniqueValidator(queryset=CustomUser.objects.all())
            ]
        )
    gov_id = serializers.CharField(
        max_length=255,
        allow_blank=True,
        validators=[is_alphanumeric]
        )

    # def validate(self, data):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'name', 'last_name', 'gov_id', 'email', 'company'
            )
        extra_kwargs = {}


from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer


class CustomRegisterSerializer(RegisterSerializer):
    """Use default serializer except don't user username"""

    username = None


class CustomLoginSerializer(LoginSerializer):
    """Use default serializer except don't user username"""

    username = None
