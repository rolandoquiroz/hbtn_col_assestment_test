
from django.urls import include, path


urlpatterns = [
    path(
        route='users/',
        view=include('users.urls'),
        ),
    path(
        route='rest-auth/',
        view=include('rest_auth.urls')
        ),
    path(
        route='rest-auth/registration/',
        view=include('rest_auth.registration.urls')
        ),
]

'''
urlpatterns = [
    path(
        route='users/',
        view=post_user,
        name='post_user'
    ),
    path(
        route='users/<int:pk>/',
        view=get_update_delete_user,
        name='get_update_delete_user'
    ),
    path(
        route='users/all/',
        view=include('users.urls')
    ),
]
'''
