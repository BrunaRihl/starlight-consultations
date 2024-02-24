from django.urls import path
from .views import create_booking, edit_booking


urlpatterns = [
   path("", create_booking, name="create_booking"),
   path("edit/<int:booking_id>", edit_booking, name="edit_booking"),
]
