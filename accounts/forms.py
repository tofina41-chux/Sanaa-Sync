from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class HubSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Add any extra fields you want them to fill out at signup here
        fields = ("username", "email", "first_name", "last_name", "phone_number")


# ADD THIS CLASS BELOW:
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone_number")     