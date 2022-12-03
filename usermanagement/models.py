from django.db import models

# Create your models here.
class SpiritualCamp(models.Model):
    full_name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    family_members = models.PositiveIntegerField()
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name