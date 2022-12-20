from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import (User, Account)
from django.views.decorators.csrf import (csrf_protect)

# Solving a Does not exists problem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate

# Authentication Are handled here !!!


class UserRegisterform(forms.ModelForm):

    # emails are set by default so i don't have to set it manually
    #email =  forms.EmailField()
    password = forms.CharField(label='Paasword', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Validation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'password2',
        ]
        exclude = ['user']

    # Check if the email has already been taken

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_check = User.objects.filter(email=email)
        if email_check.exists():
            raise forms.ValidationError('This email is taken !!!')
            # else
        return email

    # Check if the two password matches
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        # run test here
        if password != password2:
            raise forms.ValidationError('Two passwords must matches !!! ')
        return password2

    # overide the save form here  !!

    def save(self, commit=True, *args, **kwargs):
        instance = super(UserRegisterform, self).save(commit=False)
        instance.set_password(self.cleaned_data['password2'])
        if commit:
            instance.save()
        return instance

        # Log in user form

class LoginFormUser(forms.ModelForm):
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model  = User
        fields = [
            'email',
            'password'
        ]

        # Using another method here to validate user data and authenticate him  !!
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        loggedin_user = authenticate(
             email=email, password=password)
             # raise this exception if this user in none or no longer active
        if loggedin_user is None or not loggedin_user.is_active:
            raise forms.ValidationError(
                'This data are invalid please try againe !!!!')
        return self.cleaned_data

