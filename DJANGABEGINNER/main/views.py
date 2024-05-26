from django.http import JsonResponse
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
from django.views.generic.edit import CreateView


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
        print(good_slug)
        good_for_edit = get_object_or_404(Goods, slug=good_slug)
        
        
        if request.method == 'POST':
            edit_good_form = EditGoodForm(request, slug= f'{good_slug}') #товар который найден в БД по id(slug) переданному с клиента
            if edit_good_form.is_valid():
                edit_good = edit_good_form.save(commit= False)

                edit_good.save()
                return redirect('home')
            else:
                print(edit_good_form.errors)
                
        else:

            edit_good_form = EditGoodForm(instance=good_for_edit)
        
        try:

            CommentsGoods = get_object_or_404(Comments,good = good_for_edit)#slug это поля таблицы comments
       
           
        

        
        except Exception as e: 
            CommentsGoods={}
            print(f'строка: {e}')


        
        context = {
            'edit_good_form' : edit_good_form,
            'good_for_edit' :  good_for_edit,
            'CommentsGoods' : CommentsGoods,
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
    return redirect(reverse_lazy('login'))

class RegisterUserform(DataMixin, CreateView):
    form_class = RegisterUserform
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        user = form.save()
        login(self.request, user)
        return redirect('shop')
    
    def form_invalid(self, form):
        
        print(form.errors)
        return super(RegisterUserform,self).form_invalid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
    

def add_comments_view(request):
    if request.method == "POST":
        good_id = request.POST.get('good_id')
        good_for_edit_comments = get_object_or_404(Goods, pk=good_id)

        send_comment =Comments.objects.create(
            good = good_for_edit_comments,
            sender = request.user,
            message = request.POST.get('message'),
        )
    
        send_comment.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})