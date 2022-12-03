from django.db import models

#ONLY MAIN PAGE MODELS HERE **EXCLUDING LOGIN/REGISTER MODELS**

# Admin Event handling function
class Event(models.Model):
    title = models.CharField(max_length=50)
    event_date = models.DateTimeField()
    small_descripton = models.CharField(max_length=150)

    def __str__(self):
        return self.title


# Page Contact form function
class Feedback(models.Model):
    subject = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15, primary_key=True)
    message = models.TextField()

    def __str__(self):
        return self.subject    

# Page SpiritualPlayBooking form function
class SpiritualPlayBooking(models.Model):
    full_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=15, primary_key=True)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name

# Page SpiritualCampBooking form function
# class SpiritualCamp(models.Model):
#     full_name = models.CharField(max_length=200)
#     mobile_number = models.CharField(max_length=15)
#     date_of_birth = models.DateField()
#     family_members = models.PositiveIntegerField()
#     last_modified = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.full_name