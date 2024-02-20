from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile
from allauth.account.forms import LoginForm, SignupForm
from django.utils.translation import gettext_lazy as _




# UserCreationForm is built-in form provided by Django's authentication system for creating new user accounts
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'username', 'user_type', 'password1', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    

    def clean_email(self):
        data = self.cleaned_data['email']
        if CustomUser.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already registered.')
        return data
    
    
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password'].label = False
        self.fields['login'].widget = forms.TextInput(attrs={'autofocus':'true','placeholder': 'Email address'})
        self.fields['login'].label = False

    def clean(self):
        email = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')
        if email:
            self.cleaned_data['email'] = email  # Set the email as the username for authentication
        if not email or not password:
            raise forms.ValidationError('Both email and password are required.')

        return super().clean()


class CustomSignupForm(SignupForm):
    email = forms.EmailField(label=_('Email address'))
    username = forms.CharField(max_length=250, label=_('Username'))
    user_type = forms.ChoiceField(choices=CustomUser.User_Types.choices, label=_('User Type'))
    password1 = forms.CharField(widget=forms.PasswordInput, label=_('Password'))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_('Confirm Password'))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['email'].widget = forms.EmailField(attrs={'autofocus':'true','placeholder': 'Email address'})
    #     self.fields['email'].label = False
    #     self.fields['username'].widget = forms.CharField(attrs={'placeholder': 'Username'})
    #     self.fields['username'].label = False
    #     self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
    #     self.fields['password1'].label = False
    #     self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    #     self.fields['password2'].label = False

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered.')
        return email

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField() 
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','bio','image']