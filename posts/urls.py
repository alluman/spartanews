from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('create/', views.PostCreate.as_view(), name='create'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('<int:pk>/comments/',
         views.UserCommentsListView.as_view(), name='comment_list'),
    path('<int:pk>/comments/create/',
         views.CommentCreate.as_view(), name='comment_create'),
    path('<int:pk>/comments/detail',
         views.CommentDetail.as_view(), name='comment_detail'),
]
