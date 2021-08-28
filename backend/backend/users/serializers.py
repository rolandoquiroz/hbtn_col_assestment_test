from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . validators import is_alphanumeric
from . models import CustomUser


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
