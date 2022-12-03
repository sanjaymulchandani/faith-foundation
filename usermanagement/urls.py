from django.urls import path
from . import views

#ONLY LOGIN/REGISTER/LOGOUT/ACCOUNT HANDLING

urlpatterns = [
    path('register/', views.register, name = "register"),
    path('login/', views.login, name = "login"),
]