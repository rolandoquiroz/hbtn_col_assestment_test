from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path(
        route='admin/',
        view=admin.site.urls,
        ),
    path(
        route='token/access-refresh/',
        view=TokenObtainPairView.as_view(),
        name='token_obtain_access_refresh'
        ),
    path(
        route='token/refresh/',
        view=TokenRefreshView.as_view(),
        name='token_get_refresh'
        ),
    path(
        route='api/v1/',
        view=include('retail_company.urls'),
        ),
]
