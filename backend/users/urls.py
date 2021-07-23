from django.urls import include, path
from users.views import get_users

urlpatterns = [
    path(
        route='all/',
        view=get_users
        ),
]
