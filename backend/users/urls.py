from django.urls import path
from . import views


urlpatterns = [
    path(
        route='',
        view=views.post_user,
        name='post_user'
    ),
    path(
        route='<int:pk>/',
        view=views.get_user,
        name='get_user'
    ),
    path(
        route='all/',
        view=views.get_users,
        name='get_users',
        ),
]
