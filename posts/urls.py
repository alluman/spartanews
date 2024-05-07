from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('create/', views.PostCreate.as_view(), name='create'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('<int:pk>/comments/create/',
         views.CommentCreate.as_view(), name='comment'),
    path('<int:post_id>/comments/<int:comment_id>/',
         views.CommentUpdate.as_view(), name='comment_update'),
    path('comments/<int:pk>/',
         views.CommentsList.as_view(), name='comment_list'),
    path('comments/user/<int:pk>/',
         views.UserCommentsListView.as_view(), name='comment_user_list'),
    path('comments/<int:comment_id>/replies/',
         views.ReplyListAPIView.as_view(), name='reply-list'),
    path('comments/<int:comment_id>/replies/create/',
         views.ReplyCreateAPIView.as_view(), name='reply-create'),
]
