from django.conf.urls import url
from retail_company import views


urlpatterns = [
    url(
        r'^api/v1/users/$',
        views.post_user,
        name='post_user'
    ),
    url(
        r'^api/v1/users/(?P<pk>[0-9]+)$',
        views.get_update_delete_user,
        name='get_update_delete_user'
    ),
    url(
        r'^api/v1/users/all$',
        views.get_users,
        name='get_users'
    ),
]
