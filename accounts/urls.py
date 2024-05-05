from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name='accounts'
urlpatterns = [
    path('create/', views.CreateView.as_view(), name='create'),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile')
    ]
