from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)  # 제목
    content = models.TextField()  # 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간
    likes = models.PositiveIntegerField(default=0)  # 좋아요 기능

    def __str__(self):
        return self.title
