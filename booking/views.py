from django.shortcuts import render
from booking.forms import BookingForm

# Create your views here.
def page_booking(request):
   """
   Renders the about page.
   """
   form = BookingForm()
   return render(request, "booking.html", {"html_form": form})
