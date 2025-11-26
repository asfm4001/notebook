from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter
from api_v1 import views

app_name = "api_v1"

router = DefaultRouter()
router.register('', views.NoteViewSet, basename='note')

# Auth URL patterns
auth_patterns = [
    path("token/", obtain_auth_token, name='drf_token'),
    path("jwt/", TokenObtainPairView.as_view(), name='jwt_token'),
    path("jwt/refresh/", TokenRefreshView.as_view(), name='jwt_refresh'),
]

# API Docs URL patterns
docs_patterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='api_v1:schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='api_v1:schema'), name='redoc'),
]

urlpatterns = [
    path('auth/', include(auth_patterns)),
    path('notes/', include(router.urls)),
    path('docs/', include(docs_patterns)),
]