from . import views
from django.urls import path
from .views import page_booking


urlpatterns = [
   path("", page_booking, name="booking"),

]
