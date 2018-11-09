from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import froms

class SignUpForm(UserCreationForm):
    email = froms.EmailField()
    first_name = froms.CharField(max_length = 100)
    last_name = froms.CharField(max_length = 100)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
