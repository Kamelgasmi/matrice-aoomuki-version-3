from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, EmailInput, FileInput, PasswordInput, Select, CheckboxInput,RadioSelect, CheckboxSelectMultiple
from django.forms.utils import ErrorList
from django import forms
from .models import Competence, Field, Certification, Society

from .models import User
# from .models import ListWorkstation, Society

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('is_collaborater', 'workstation', 'society',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('is_collaborater', 'workstation', 'society', )

class AddUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["last_name", "first_name", "username", 'email', 'is_superuser', 'is_staff','is_collaborater', 'workstation', 'society']
