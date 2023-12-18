from django.shortcuts import redirect, render
from.forms import ContactMeForm
from .models import *
# Create your views here.

def home_view(request):
    posts = Posts.objects.order_by('-id')
    return render(request, 'main/home.html', {'posts': posts})


def index(request):
    error = ''
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('home')
        else:
            error = 'ошибка'
    else:
        form = ContactMeForm()
    
    context = {
        'title' : 'Главная страница сайта',
        'error' : error,
        'form'  : form,
    }
    return render(request, 'main/home.html', context)

def shop_view(request):
    goods = Goods.objects.order_by('-id')
    return render(request, 'main/shop.html', {'goods': goods})