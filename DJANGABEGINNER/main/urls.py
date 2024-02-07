from django import views
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns=[
#  path('', views.index, name='home'),
    path('', views.shop_view, name='shop'),
    path('add_good/', views.addgood, name='add_good'),
    path('edit_good/<slug:good_slug>/', views.edit_goods_view, name='edit_good')
    ]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
