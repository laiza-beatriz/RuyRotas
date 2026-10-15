# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from .models import Perfil

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

class PerfilForm(forms.ModelForm):
    nome = forms.CharField(
        max_length=150,
        label="nome",
        widget=forms.TextInput(attrs={"class": "form-control profile-input", "placeholder": "seu nome"}),
    )

    class Meta:
        model = Perfil
        fields = ["foto", "matricula"]
        widgets = {
            "foto": forms.FileInput(attrs={"class": "d-none", "accept": "image/*", "id": "id_foto"}),
            "matricula": forms.TextInput(attrs={"class": "form-control profile-input", "placeholder": "sua matrícula"}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        if user:
            self.fields["nome"].initial = user.get_full_name() or user.username

    def save(self, commit=True):
        perfil = super().save(commit=False)
        nome = self.cleaned_data["nome"].strip()
        partes = nome.split(" ", 1)
        self.user.first_name = partes[0]
        self.user.last_name = partes[1] if len(partes) > 1 else ""
        if commit:
            self.user.save()
            perfil.save()
        return perfil