from django import views
from django.urls import path
from . import views


urlpatterns=[
#  path('', views.index, name='home'),
    path('', views.shop_view, name='shop'),
]
