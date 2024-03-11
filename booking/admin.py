from django.contrib import admin
from booking.models import Booking


class BookingAdmin(admin.ModelAdmin):
    """
    Customizes the display of booking information in the Django admin interface.

    Attributes:
    list_display (list): Specifies the fields to display in the admin list view.
    """

    list_display = [
        "user",
        "display_service",
        "booking_date",
        "booking_time",
        "message",
    ]

    def display_service(self, obj):
        """
        Displays the name of the service associated with the given booking.

        Args:
        obj (Booking): The booking object.

        Returns:
        str: The name of the associated service.
        """
        return obj.service.name if obj.service else None

    display_service.short_description = "Service"


admin.site.register(Booking, BookingAdmin)
