from django import views
from django.urls import include, path
from . import views
from django.conf import settings 
from django.conf.urls.static import static
from .views import *

urlpatterns=[
#  path('', views.index, name='home'),
    path('', views.shop_view, name='shop'),
    path('add_good/', views.addgood, name='add_good'),
    path('edit_good/<slug:good_slug>/', views.edit_goods_view, name='edit_good'),
    path('login/', LoginUser.as_view(), name= 'login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/',RegisterUserform.as_view(), name='register'),
    path('add_comments/', views.add_comments_view, name= 'add_comments'),
    ]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
