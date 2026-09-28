# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class CadastroForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nome",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu primeiro nome'})
    )
    last_name = forms.CharField(
        label="Sobrenome",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu sobrenome'})
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seuemail@exemplo.com'})
    )

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'class': 'form-control-custom', 'placeholder': 'Digite seu e-mail'})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control-custom', 'placeholder': 'Digite sua senha'})
    )