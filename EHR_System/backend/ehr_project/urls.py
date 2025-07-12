from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # This sends any request starting with 'api/' to your api app's urls.py
    path('api/', include('api.urls')),
    # This is the specific URL for getting a login token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]