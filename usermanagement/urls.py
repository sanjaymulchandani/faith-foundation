from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = "register"),
    path('forms/', views.form_view, name="forms")
]