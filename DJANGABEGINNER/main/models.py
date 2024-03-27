from collections.abc import Iterable
from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import transliterate


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
     product_description = models.TextField('Описание', null=True, blank=True,)
     date_of_staging = models.DateField('Дата поставки', null=True, blank=True, default=datetime.now)
     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Постовщик')
     price = models.FloatField('Цена',max_length= 50, null=True, blank=True,)
     slug = models.SlugField(max_length = 200, unique = True, db_index = True, null = True, blank = True)
     
     def __str__(self) -> str:
        return f'{self.name}{self.price}'
     
     def save(self, *args, **kwargs):
         print('Saving goods....')

         slug_text = f'{self.name}-{self.pk}'
         self.slug = slugify(transliterate.translit(slug_text, reversed=True) )

         user = kwargs.pop('user', None)
         if user:
            self.author = user

         super(Goods, self).save(*args, **kwargs)
         print('Goods saved.')
     

     class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

      


class Image(models. Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name= 'images', null=True, verbose_name='Товар',)
    image = models.ImageField('Изоображение', null = True, upload_to='images/', blank=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name ='Дата загрузки',)
    file_name = models.TextField('Имя файла', null= True, blank= True,)

    class Meta():
      verbose_name = 'Файлы'  
      verbose_name_plural = 'Файлы'