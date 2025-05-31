from django.forms import ModelForm
from .models import Room , User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}  # Remove help texts for all fields
        error_messages = {
            'username': {
                'unique': "This username is already taken. Please choose a different one."
            },
            'email': {
                'unique': "This email is already registered. Please use a different email."
            }
        }









class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username','email','bio']


