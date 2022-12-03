from django.shortcuts import render
from django.contrib import messages
from .forms import BookingEngine, Contact
# Create your views here.
def home(request):
    return render(request, "index.html")
def spiritualcamp(request):
    return render(request, 'spiritualcamp.html')
def spiritualplays(request):
    return render(request, 'spiritualplays.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    context = {}
    form = Contact(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Feedback Submitted!')        
        form.save()

    context['form']= form
    return render(request, 'contact.html', context)




def spiritualcamp_register(request):
    return render(request, 'spiritual_life_camp_register.html')


def spiritualplays_register(request):
    context = {}
    form = BookingEngine(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Form submission successful!')        
        form.save()

    context['form']= form
    return render(request, 'spiritual_plays_register.html', context)
