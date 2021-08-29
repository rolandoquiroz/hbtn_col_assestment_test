'''
from django.core.validators import validate_email
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.validators import is_alphanumeric
from user.models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        min_length=2,
        max_length=255,
        validators=[is_alphabetic]
    )
    last_name = serializers.CharField(
        min_length=2,
        max_length=255,
        validators=[is_alphabetic]
    )
    gov_id = serializers.CharField(
        max_length=255,
        validators=[
            is_alphanumeric,
            UniqueValidator(queryset=User.objects.all())
            ]
        )
    email = serializers.EmailField(
        max_length=255,
        validators=[
            validate_email,
            UniqueValidator(queryset=User.objects.all())
            ]
        )
    company = serializers.CharField(
        max_length=255,
        allow_blank=True
    )
    # def validate(self, data):
    class Meta:
        model = User
        fields = (
            'id',
            'name', 'last_name', 'government_issued_id', 'email', 'company'
            )
        extra_kwargs = {}
'''