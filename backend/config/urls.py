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
        route='token/both/',
        view=TokenObtainPairView.as_view(),
        name='token_obtain_pair'
        ),
    path(
        route='token/access/',
        view=TokenRefreshView.as_view(),
        name='token_get_access'
        ),
    path(
        route='api/v1/',
        view=include('retail_company.urls'),
        ),
]
