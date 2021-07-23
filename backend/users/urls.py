from django.urls import path
from users.views import get_users

urlpatterns = [
    path(
        route='all/',
        view=get_users,
        name='get_users',
        ),
]
