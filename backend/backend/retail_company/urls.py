from django.urls import include, path


urlpatterns = [
    path(
        route='users/',
        view=include('users.urls'),
        ),
]
