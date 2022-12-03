from django.contrib import admin
from .models import Event,Feedback, SpiritualPlayBooking
# Register your models here.
admin.site.register([Event, Feedback, SpiritualPlayBooking])
