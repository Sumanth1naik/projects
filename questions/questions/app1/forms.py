from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']

class Question(ModelForm):
    class Meta:
        model=questions
        fields='__all__'
    

