from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('spiritual-camp', views.spiritualcamp, name = "spiritualcamp"),
    path('spiritual-camp-register', views.spiritualcamp_register, name = "spiritual-camp-register"),
    path('spiritual-plays-register', views.spiritualplays_register, name = "spiritual-plays-register"),
    path('spiritual-plays', views.spiritualplays, name = "spiritualplays"),
    path('about-us', views.about, name = "about"),    
    path('contact-us', views.contact, name = "contact"),    
]