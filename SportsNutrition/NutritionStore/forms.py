from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя')
    last_name = forms.CharField(label='Фамилия')
    first_name = forms.CharField(label='Имя')
    password1 = forms.CharField(label='Введите пароль', required=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', required=False, widget=forms.PasswordInput)
    email = forms.EmailField(required=True, error_messages='')
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'password1', 'password2')
