from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.urls import reverse_lazy
from django.template import loader
from django.views import generic,View
from django.contrib.auth.views import LoginView


class RegisterView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('homepage')
    template_name = "registration/register.html"

def homepage(request):
    return render(request, 'registration/login.html')

