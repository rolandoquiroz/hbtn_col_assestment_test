from rest_framework import serializers


def is_alphanumeric(value: str):
    if not value.isalnum():
        raise serializers.ValidationError('This field must be alphanumeric.')
