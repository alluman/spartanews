from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateView.as_view(), name='create'),
    ]
