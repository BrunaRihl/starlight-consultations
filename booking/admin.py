from django.contrib import admin
from booking.models import Booking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "display_service",
        "booking_date",
        "booking_time",
        "message",
    ]

    def display_service(self, obj):
        """
        Displays the name of the service associated with the given object.
        """
        return obj.service.name if obj.service else None

    display_service.short_description = "Service"


admin.site.register(Booking, BookingAdmin)