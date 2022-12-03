from django.shortcuts import render
from django.contrib import messages
from .forms import BookingEngine, Contact
# Create your views here.

# URL HANDLING ONLY


def home(request):
    return render(request, "index.html")
def spiritualcamp(request):
    return render(request, 'spiritualcamp.html')
def spiritualplays(request):
    return render(request, 'spiritualplays.html')
def about(request):
    return render(request, 'about.html')


# URL HANDLING ENDS HERE


# FORM AND OTHER FUNCTIONS


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


# def form_view(request):
#     context = {}
#     form = SpiritualCampForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()

#     context['form']= form
#     return render(request, 'forms.html', context)



def spiritualplays_register(request):
    context = {}
    form = BookingEngine(request.POST or None, request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Form submission successful!')        
        form.save()

    context['form']= form
    return render(request, 'spiritual_plays_register.html', context)



# FORM AND OTHER FUNCTIONS ENDS HERE