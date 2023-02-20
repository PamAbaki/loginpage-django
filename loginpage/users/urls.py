from django.urls import path
from .views import RegisterView
from users import views 
from . import views

  


urlpatterns = [
    #path("", views.homepage, name="homepage"),
    
    #path("login", views.login_request, name="login"),
    path("register/", RegisterView.as_view(), name="register")
]
