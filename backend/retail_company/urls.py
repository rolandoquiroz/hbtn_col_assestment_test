from django.urls import path
from retail_company.views import post_user, get_update_delete_user, get_users


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
        view=get_users,
        name='get_users'
    ),
]
