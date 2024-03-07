from django.db import models
from django.contrib.auth.models import User
from service.models import Service


# Create your models here.
class Booking(models.Model):
   user = models.ForeignKey(
       User, on_delete=models.CASCADE, related_name="booking_user"
   )
   service = models.ForeignKey(
       Service, on_delete=models.CASCADE, related_name="booking_service"
   )
   booking_date = models.DateField(null=False, blank=False)
   booking_time = models.CharField(null=False, blank=False, max_length=5)
   message = models.CharField(null=True, max_length=200)
    