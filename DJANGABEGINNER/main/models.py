from django.db import models

# Create your models here.
class Posts(models. Model):
    title = models.TextField('название поста', max_length= 50)
    post = models.TextField('пост')

    def __str__(self) -> str:
        return f'{self.title}{self.post}'
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'