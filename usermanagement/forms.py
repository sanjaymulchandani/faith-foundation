from django import forms
from .models import SpiritualCamp
# creating a form
class SpiritualCampForm(forms.ModelForm):
    class Meta:
        model = SpiritualCamp
        fields = "__all__"