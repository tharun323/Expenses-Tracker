from django import forms
from . models import Item
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class ItemModelForm(forms.ModelForm):

    class Meta:
        model=Item
        fields=('name','price','image')



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    password1 = forms.CharField(widget=forms.PasswordInput,help_text="Min 8 characters,should contain special charecters , alphabets and Numbers ")
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )