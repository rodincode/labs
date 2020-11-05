from django.urls import path
from . import views

# SET THE NAMESPACE!

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    path('', views.loginview, name='login'),
]