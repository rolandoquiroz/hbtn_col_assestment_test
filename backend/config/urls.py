from django.contrib import admin
from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('retail_company.urls')),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]
