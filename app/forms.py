from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from .models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Tài khoản', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Mật khẩu', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label='Mật khẩu hiện tại',widget=forms.PasswordInput(attrs={'autofocus': 'True','autocomplete':'current-password','class':'form-control'}))
    new_password1=forms.CharField(label='Mật khẩu mới',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
    new_password2=forms.CharField(label='Xác nhận mật khẩu mới',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label='Email',max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label='Mật khẩu mới',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
    new_password2=forms.CharField(label='Xác nhận mật khẩu mới',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
