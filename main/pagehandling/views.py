from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")
def spiritualcamp(request):
    return render(request, 'spiritualcamp.html')
def spiritualplays(request):
    return render(request, 'spiritualplays.html')
def photogallery(request):
    return render(request, 'photogallery.html')
def about(request):
    return render(request, 'about.html')