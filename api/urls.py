from django.urls import path, include

default_api_version = 'api_v1_0'

urlpatterns = [
    path('', include(f'{default_api_version}.urls')),
    path('v1.0/', include('api_v1_0.urls')),
]
