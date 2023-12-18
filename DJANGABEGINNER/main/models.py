from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models. Model):
    title = models.TextField('название поста', max_length= 50)
    post = models.TextField('пост')

    def __str__(self) -> str:
        return f'{self.title}{self.post}'
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class ContactMe(models. Model):
     name = models.TextField('Название', max_length= 50)
     email = models.TextField('Описание', max_length= 50)
     message = models.TextField('сообщение')

     def __str__(self) -> str:
        return self.name
     
     class Meta():
        verbose_name = 'Напишите мне'
        verbose_name_plural = 'Сообщения - напишите мне'

     
class Goods(models. Model):
     name = models.TextField('Название', max_length= 50)
     product_description = models.TextField('Описание', max_length= 50)
     date_of_staging = models.DateField('Дата поставки', null=True, blank=True, default=datetime.now)
     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Постовщик')

     def __str__(self) -> str:
        return self.name
     
     class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'