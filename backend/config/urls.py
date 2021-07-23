from django.contrib import admin
# from rest_framework.authtoken.views import obtain_auth_token
from django.urls import include, path


urlpatterns = [
    path(
        route='admin/',
        view=admin.site.urls,
        ),
    path(
        route='api/v1/',
        view=include('retail_company.urls'),
        ),
]

'''
    path(
        route='api-auth/',
        view=include('rest_framework.urls'),
        ),
    path(
        route='api/v1/dj-rest-auth/',
        view=include('dj_rest_auth.urls'),
        name='dj-rest-auth',
        ),
'''
