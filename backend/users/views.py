# from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import api_view
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from users.serializers import CustomUserSerializer

'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_user(request):
    # insert a new record for a user
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'last_name': request.data.get('last_name'),
            'government_issued_id': request.data.get('government_issued_id'),
            'email': request.data.get('email'),
            'company': request.data.get('company')
        }
        serializer = UserSerializer(data=data)
        # form validation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def get_update_delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # update details of a single user
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single user
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


@api_view(['GET'])
def get_users(request):
    # get all users
    if request.method == 'GET':
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
