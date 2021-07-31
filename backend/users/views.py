from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import CustomUser
from . serializers import CustomUserSerializer


@api_view(['POST'])
def post_user(request):
    # insert a new record for a user
    if request.method == 'POST':
        data = {
            'email': request.data.get('email'),
            'name': request.data.get('name'),
            'last_name': request.data.get('last_name'),
            'gov_id': request.data.get('gov_id'),
            'company': request.data.get('company')
        }
        serializer = CustomUserSerializer(data=data)
        # form validation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single user
    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
def get_users(request):
    # get all users
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
