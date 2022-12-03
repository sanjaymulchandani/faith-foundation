from django.shortcuts import render
from .forms import SpiritualCampForm

# Create your views here.
def register(request):
    return render(request, 'register.html')


def form_view(request):
    context = {}
    form = SpiritualCampForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request, 'forms.html', context)
