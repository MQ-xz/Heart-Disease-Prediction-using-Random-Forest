from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import History


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class HealthCheckForm(forms.ModelForm):

    class Meta:
        model = History
        fields = '__all__'
