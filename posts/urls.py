from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('', views.CreateView.as_view(), name='create'),
    ]
