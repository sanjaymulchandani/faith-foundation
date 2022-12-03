from django.shortcuts import render
from .forms import SpiritualCampForm

# Create your views here. ONLY LOGIN/REGISTER/LOGOUT/ACCOUNT HANDLING
def register(request):
    return render(request, 'register.html')


