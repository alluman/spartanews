from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, get_object_or_404
from .serializers import ArticleSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


def index(request):
    order = request.GET.get('order', 'latest')
    query = request.GET.get('query', '')

    if order == 'oldest':
        articles = Article.objects.all().order_by('created_at')
    else:
        articles = Article.objects.all().order_by('-created_at')

    if query:
        # 제목에서 검색어를 포함하는 기사만 필터링
        articles = articles.filter(title__icontains=query)

    return render(request, 'index.html', {'articles': articles})


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        article = self.get_object()
        article.likes += 1
        article.save()
        return Response({'success': True, 'likes': article.likes})
