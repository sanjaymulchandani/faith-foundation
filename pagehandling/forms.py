from django import forms
from .models import Event, Feedback, SpiritualPlayBooking
#SpiritualCampForm_Admin

class Camp(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

class Contact(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

class BookingEngine(forms.ModelForm):
    class Meta:
        model = SpiritualPlayBooking
        fields = "__all__"