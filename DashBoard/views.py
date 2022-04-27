from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.views import View
from .forms import *


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, template_name='auth/home.html')
    return redirect('/detail')


class Login(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request=request, template_name="auth/login.html", context={"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect(index)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")


class Register(View):
    def get(self, request):
        form = NewUserForm()
        return render(request=request, template_name="auth/register.html", context={"form": form})

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect(index)
        else:
            messages.error(request, "Invalid username or password.")
            return render(request=request, template_name="auth/register.html", context={"form": form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(index)


class Detail(View):
    def get(self, request):
        form = DetailForm()
        return render(request=request, template_name="main/details.html", context={"form": form})

    def post(self, request):
        form = DetailForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
            return redirect('.')
        else:
            messages.error(request, form.errors)
            return render(request=request, template_name="main/details.html", context={"form": form})
