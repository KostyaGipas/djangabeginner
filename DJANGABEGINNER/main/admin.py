from django.contrib import admin
from .models import *
# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name','date_of_staging', 'author', 'price',]

class ImageAdmin(admin.ModelAdmin):
    list_display = ['good','image', 'created_at',]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['good','sender', 'message','created_at',]




admin.site.register(Posts)
admin.site.register(ContactMe)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comments, CommentAdmin)
