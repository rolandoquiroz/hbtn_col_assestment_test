
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
]
