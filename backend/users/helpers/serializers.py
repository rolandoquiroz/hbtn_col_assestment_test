from dj_rest_auth.serializers import LoginSerializer


class CustomLoginSerializer(LoginSerializer):
    """Use default serializer except don't user username"""
    username = None
