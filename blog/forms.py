from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.Form):
    name = forms.CharField(label="Enter the blog name", max_length=100)
    tagline = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


