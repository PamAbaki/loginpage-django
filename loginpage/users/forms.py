from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Details




# Create your forms here.

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    # Override the help_text of username, password1 and password2 fields
    username = forms.CharField(help_text='', required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), help_text='', required=True)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'}), help_text='', required=True)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
            # Create a Details instance for the newly registered user
            details = Details.objects.create(
                username=user.username,
                password=user.password,
                password_confirmation=self.cleaned_data.get('password2')
            )
        return user

