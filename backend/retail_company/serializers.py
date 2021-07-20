from rest_framework import serializers
from retail_company.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name', 'last_name', 'government_issued_id', 'email', 'company'
            )
