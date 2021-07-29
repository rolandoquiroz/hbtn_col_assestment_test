from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path(
        route='admin/',
        view=admin.site.urls,
        ),
    path(
        route='api-auth/',
        view=include('rest_framework.urls'),
        ),
    path(
        route='api/v1/dj-rest-auth/',
        view=include('dj_rest_auth.urls')
        ),
    path(
        route='api/v1/',
        view=include('retail_company.urls'),
        ),
    path(
        route='auth-jwt/',
        view=obtain_jwt_token
        ),
    path(
        route='auth-jwt-refresh/',
        view=refresh_jwt_token
        ),
    path(
        route='auth-jwt-verify/',
        view=verify_jwt_token
        ),
]
