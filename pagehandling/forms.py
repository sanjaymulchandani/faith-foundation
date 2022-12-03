from django import forms
from .models import Event, Feedback, SpiritualPlayBooking

#SpiritualCampForm _ ADMIN SIDE ONL
class Camp(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

#CONTACT/FEEDNACK FORM 
class Contact(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

#PLAY BOOKING ENGINE 
class BookingEngine(forms.ModelForm):
    class Meta:
        model = SpiritualPlayBooking
        fields = "__all__"

#SPIRITUAL CAMP FORM
# class SpiritualCampForm(forms.ModelForm):
#     class Meta:
#         model = SpiritualCamp
#         fields = "__all__"