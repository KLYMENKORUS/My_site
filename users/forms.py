import datetime

from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=False, help_text='YYYY-MM-DD')

    class Meta:
        model = Profile
        fields = ['photo', 'date_of_birth', 'about_myself']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control', }))
    first_name = forms.CharField(max_length=100, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First name',
                                                               'class': 'form-control', }))
    email = forms.EmailField(max_length=50, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control', }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)
