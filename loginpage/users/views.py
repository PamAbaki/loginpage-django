from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate 
from django.contrib import messages,auth
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic,View
from django.contrib.auth.models import User
from users.models import Profile

class RegisterView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password1=request.POST['password1']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'email already exist')
                return redirect('register/')
            else:
                user=User.objects.create_user(username=username,password1=password1)
                user.save()

                user_model=user.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('login/')

        else:
            messages.info(request,'passwords do not much')
            return redirect('register/')

    else:     
        return render(request,'registration/register.html')


def login(request):
    return render(request,'registration/login.html')
