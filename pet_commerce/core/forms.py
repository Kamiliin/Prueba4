from django import forms
from .models import CustomUser, Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

class UserForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label='Confirmación de contraseña',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='Enter the same password as before, for verification.',
    )

    class Meta:
        model = CustomUser
        fields = ('name', 'password1', 'password2', 'email', 'comments',)

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"


class ProductDeleteForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = []


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"

class CategoryDeleteForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = []