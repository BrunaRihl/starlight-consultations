from django.db import models
from django.contrib.auth.models import User
from service.models import Service


class Booking(models.Model):
    """
    Model to store information about service bookings.
    This class represents a booking made by a user for a specific service.
    Each booking is associated with a user and a specific service.
    **Attributes**
    `user` (:class:`~django.contrib.auth.models.User`): The user who made the booking.
    `service` (:class:`~service.models.Service`): The booked service.
    `booking_date` (:obj:`datetime.date`): The date of the booking.
    `booking_time` (:obj:`str`): The time of the booking.
    `message` (:obj:`str`, optional): An optional message associated with the booking.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_user"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="booking_service"
    )
    booking_date = models.DateField(null=False, blank=False)
    booking_time = models.CharField(null=False, blank=False, max_length=5)
    message = models.CharField(null=True, max_length=200)



