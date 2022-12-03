from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    event_date = models.DateTimeField()
    small_descripton = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    subject = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15)
    message = models.CharField(max_length=500)

class SpiritualPlayBooking(models.Model):
    full_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=500)