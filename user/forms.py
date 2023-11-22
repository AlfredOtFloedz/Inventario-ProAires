from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2',
        ]
        labels = {
            'username' : 'Nombre de Usuario',
            'email' : 'Correo Electrónico',
            'password1':'Contraseña',
            'password2':'Contraseña',
        }
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'email',
        ]
        labels ={
            'username':'Nombre de Usuario',
            'email':'Correo Electrónico',
        }
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'address', 'phone', 'image',
        ]
        labels = {
            'address':'Dirección',
            'phone':'Teléfono',
            'image':'Foto de Perfil',
        }