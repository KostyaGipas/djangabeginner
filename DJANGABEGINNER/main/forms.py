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