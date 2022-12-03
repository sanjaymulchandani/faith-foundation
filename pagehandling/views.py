from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")
def spiritualcamp(request):
    return render(request, 'spiritualcamp.html')
def spiritualplays(request):
    return render(request, 'spiritualplays.html')
def about(request):
    return render(request, 'about.html')
def about(request):
    return render(request, 'contact.html')
def spiritualcamp_register(request):
    return render(request, 'spiritual_life_camp_register.html')
def spiritualplays_register(request):
    return render(request, 'spiritual_plays_register.html')
