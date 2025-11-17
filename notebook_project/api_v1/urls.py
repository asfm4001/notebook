from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api_v1 import views

app_name = "api_v1"

urlpatterns = [
    path("token/", obtain_auth_token, name='DRF_token'),
    path("jwt_token/", TokenObtainPairView.as_view(), name='jwt_token'),
    path("jwt_refresh/", TokenRefreshView.as_view(), name='jwt_refresh'),
    path('notes/', views.NoteRouterView.as_view(), name='notes'),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='note'),
]