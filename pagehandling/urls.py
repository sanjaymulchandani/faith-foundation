from django.urls import path
from . import views

#URLS HANDLING ONLY FOR MAIN PAGES **LOGIN/REGISTER URLS ARE EXCLUDED**

urlpatterns = [
    path('', views.home, name = "home"),
    path('about-us', views.about, name = "about"),    
    path('contact-us', views.contact, name = "contact"),
    path('spiritual-camp', views.spiritualcamp, name = "spiritualcamp"),
    path('spiritual-plays', views.spiritualplays, name = "spiritualplays"),
    path('spiritual-camp-register', views.spiritualcamp_register, name = "spiritual-camp-register"),
    path('spiritual-plays-register', views.spiritualplays_register, name = "spiritual-plays-register"),
]