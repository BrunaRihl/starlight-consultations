from django.urls import path
from .views import create_booking, edit_booking, delete_booking


"""
Defines URL patterns for the 'booking' app.

This module contains URL patterns for directing requests to the appropriate views
in the 'booking' app.

**URL Patterns**
- '' : Directs to the 'create_booking' view defined in the 'views' module.
- 'edit/<int:booking_id>' : Directs to the 'edit_booking' view defined in the 'views' module.
- 'delete/<int:booking_id>' : Directs to the 'delete_booking' view defined in the 'views' module.
"""
urlpatterns = [
   path("", create_booking, name="create_booking"),
   path("edit/<int:booking_id>", edit_booking, name="edit_booking"),
   path("delete/<int:booking_id>", delete_booking, name="delete_booking"),
]
