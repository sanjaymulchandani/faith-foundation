from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('spiritual-camp', views.spiritualcamp, name = "spiritualcamp"),
    path('spiritual-plays', views.spiritualplays, name = "spiritualplays"),
    path('photo-gallery', views.photogallery, name = "photogallery"),
    path('about-us', views.about, name = "about"),    
    path('contact-us', views.about, name = "contact"),    
]