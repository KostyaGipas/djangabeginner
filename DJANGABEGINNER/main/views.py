from django.shortcuts import render
from .models import *
# Create your views here.

def home_view(request):
    posts = Posts.objects.order_by('-id')
    return render(request, 'main/home.html', {'posts': posts})
