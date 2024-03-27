
from. models import *
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class ContactMeForm(ModelForm):
    class Meta:
        model = ContactMe
        fields=["name", "email", "message"] 
        widgets = {
            "name":TextInput(attrs={
                'name': 'name',
                'id' : 'name',
                'type': 'text',
                'placeholder': 'Введите имя',
            }),
            
            "email":TextInput(attrs={
                'name': 'email',
                'id' : 'email',
                'type': 'text',
                'placeholder': 'Введите email',
            }),

            "message":Textarea(attrs={
                'name': 'message',
                'id' : 'message',
                'type': 'text',
                'placeholder': 'Введите сообщение',
            }),
        }

class AddGoodForm(ModelForm):
    class Meta:
        model = Goods
        fields=["name", "product_description", "date_of_staging", "price",]
        widgets= {
             "name":TextInput(attrs={   
                'name': 'name',
                'class': 'form-control mt-1',
                'id' : 'name_id',
                'type': 'text',
                'placeholder': 'Введите название товара',
            }),

            "product_description":Textarea(attrs={
                'name': 'product_description',
                'class': 'form-control mt-1',
                'id' : 'product_description_id',
                'type': 'text',
                'placeholder': 'Введите описание товара',
            }),

             "date_of_staging":TextInput(attrs={
                'name': 'date_of_staging',
                'id' : 'date_of_staging_id',
                'class': 'form-control mt-1',
                'type': 'text',
                'placeholder': 'Введите дату поставки товара',
            }),

            "price":TextInput(attrs={
                'name': 'price',
                'class': 'form-control mt-1',
                'id' : 'price_id',
                'type': 'text',
                'placeholder': 'Введите цену товара',
            }),
           
        }

class EditGoodForm(ModelForm):
    class Meta:  
        model = Goods
        fields=["name", "product_description", "date_of_staging", "price",]
        widgets= {
             "name":TextInput(attrs={   
                'name': 'name',
                'class': 'form-control mt-1',
                'id' : 'name_id',
                'type': 'text',
                'placeholder': 'Введите название товара',
            }),

            "product_description":Textarea(attrs={
                'name': 'product_description',
                'class': 'form-control mt-1',
                'id' : 'product_description_id',
                'type': 'text',
                'placeholder': 'Введите описание товара',
            }),

             "date_of_staging":TextInput(attrs={
                'name': 'date_of_staging',
                'id' : 'date_of_staging_id',
                'class': 'form-control mt-1',
                'type': 'text',
                'placeholder': 'Введите дату поставки товара',
            }),

            "price":TextInput(attrs={
                'name': 'price',
                'class': 'form-control mt-1',
                'id' : 'price_id',
                'type': 'text',
                'placeholder': 'Введите цену товара',
            }),
           
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget = forms.TextInput(attrs={
        'type' :  'text',
        'class' : 'form-control',
        'placeholder' : 'Введите логин',
        'name' : 'login',
        'id' : 'login_id',}))
    password = forms.CharField(label='пароль', widget = forms.PasswordInput(attrs={
         'type' :  'password',
        'class' : 'form-control',
        'placeholder' : 'Введите пароль',
        'name' : 'password_login',
        'id' : 'password_login_id',
    }))