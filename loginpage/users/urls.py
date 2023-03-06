from django.urls import path
from .views import RegisterView
from users import views 
from . import views
from django.views.generic.base import TemplateView


  


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('page/', TemplateView.as_view(template_name='mypage.html'), name='page'),
    path("register/", RegisterView.as_view(), name="register")
]
