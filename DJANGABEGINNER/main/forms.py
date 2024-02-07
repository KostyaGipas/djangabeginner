from. models import *
from django.forms import ModelForm, TextInput, Textarea


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

