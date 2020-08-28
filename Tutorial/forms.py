from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Form used for Registration of new users
class RegisterForm(UserCreationForm):
    class Meta:
        model = User          # Default user model of Django
        fields = ['username','email','password1','password2']  # See documentation for more field details and names
        # Widgets are used for customization of form attr. in css or elsewhere
        widgets = {
             'username': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
             'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
             'password1': forms.TextInput(),
             'password2': forms.TextInput(),

         }


