from django.contrib import admin
from django.urls import path, include
from articles import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('create/', views.article_create, name='article_create'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
