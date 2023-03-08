from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate 
from django.urls import reverse_lazy
from django.views import generic


class RegisterView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('homepage')
    template_name = "registration/register.html"

def homepage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log in the user and redirect to the homepage
                login(request, user)
                return redirect('page')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



@login_required
def page(request):
    return render(request, 'mypage.html')