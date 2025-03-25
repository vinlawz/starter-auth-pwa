from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import ResetPasswordForm, SignupForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """Form for creating a new user"""

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):
    """Form for updating user information"""

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class CustomSignupForm(SignupForm):
    """Custom Signup Form for allauth"""

    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    def save(self, request):
        """Save method to store user data"""
        user = super().save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()
        return user


class CustomResetPasswordForm(ResetPasswordForm):
    """Custom Reset Password Form"""

    custom_field = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Custom Field'})
    )

    def clean_custom_field(self):
        """Validate custom field"""
        custom_value = self.cleaned_data.get('custom_field')
        if custom_value and len(custom_value) < 5:
            raise forms.ValidationError("Custom field must be at least 5 characters.")
        return custom_value
