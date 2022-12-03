from django.shortcuts import render

# Create your views here. ONLY LOGIN/REGISTER/LOGOUT/ACCOUNT HANDLING
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

