from os import pread
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.views import View
from .forms import *
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))


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
        features = []
        for key, value in request.POST.items():
            features.append(value)
        features = [float(i) for i in features[1:]]

        array_features = np.array([features])
        prediction = model.predict(array_features)
        x = model.predict_proba(array_features)
        pos = x[0][1]
        pos = pos * 100
        print(prediction[0], pos)

        data = request.POST.copy()
        data['pos'] = pos
        data['target'] = prediction[0]
        data['user'] = request.user.id
        form = DetailForm(data)

        if form.is_valid():
            # form.save()
            if pos > 70:
                messages.error(request, f'Probablity of having heart disease: {pos}% \n Risk of having heart disease: HIGH')
            elif pos > 40:
                messages.warning(request, f'Probablity of having heart disease: {pos}% \n Risk of having heart disease: MEDIUM')
            else:
                messages.success(request, f'Probablity of having heart disease: {pos}% \n Risk of having heart disease: LOW')
        else:
            messages.error(request, form.errors)
        return render(request=request, template_name="main/details.html", context={"form": form})
