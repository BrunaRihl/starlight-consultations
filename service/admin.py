from django.contrib import admin
from booking.models import Service


"""
Registers the Service model with the Django admin interface.

This module defines a custom admin interface for the Service model.

"""


class ServiceAdmin(admin.ModelAdmin):
    """
    Customizes the display of Service model instances in the Django
    admin interface.

    **Attributes**
    - `list_display` : Determines the fields to display in the admin
    interface list view.
    """

    list_display = [
        "name",
        "consultant",
    ]


# Register the Service model with the ServiceAdmin customizations
admin.site.register(Service, ServiceAdmin)
