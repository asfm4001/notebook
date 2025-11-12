from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views

app_name = "users"

urlpatterns = [
    path('register/', views.RegisterCreateView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]