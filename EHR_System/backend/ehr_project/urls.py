from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token # Make sure this is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # This line creates the login API endpoint. It must be present.
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]