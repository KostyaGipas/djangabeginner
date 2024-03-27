from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .utils import *
from.forms import *
from .models import *
import uuid
from django.utils.text import slugify
from PIL import Image as PILImage
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView


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

def addgood(request):
    if request.method == 'POST':

        add_goods_form = AddGoodForm(request.POST)

        if add_goods_form.is_valid():
            the_goods = add_goods_form.save(commit = False)
            the_goods.author = request.user


            the_goods.save()

            image_files= request.FILES.getlist('image')          

            for image_file in image_files:
                PILImage.open(image_file)
                fs = FileSystemStorage()
                unique_filename = f"{uuid.uuid4()}_{slugify(image_file.name)}"
                file_name = fs.save(unique_filename, image_file)
                image_path = fs.url(file_name)


                image = Image.objects.create(
                    good = the_goods,
                    image = image_path,
                    file_name = file_name,
                )

                print('Этот Image', image)

            return redirect('shop')
        else:
            print(add_goods_form.errors)
    else:
        add_goods_form = AddGoodForm()
    
    context = {
        'add_goods_form' : add_goods_form,
        
    }

    return render(request, 'main/add_goods.html', context)

@login_required
def edit_goods_view(request, good_slug):
    try: 
        good_for_edit = get_object_or_404(Goods, slug=good_slug)
        if request.POST:
            edit_good_form = EditGoodForm(request.POST, instance=good_for_edit)
        else:
            edit_good_form = EditGoodForm(instance=good_for_edit)
        
        context = {
            'edit_good_form' : edit_good_form,
             'good_for_edit' :  good_for_edit,
        }

        return render(request, 'main/edit_goods.html', context)

    except Exception as e:
        print(f'строка: {e}')
    
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    #def get_context_data(self, *, object_list= None 

    def get_success_url(self):
        return reverse_lazy('shop')
      

def logout_user(request):
    logout(request)
    return render(request, 'main/login.html')