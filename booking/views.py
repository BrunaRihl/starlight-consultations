import datetime

from django.shortcuts import render, get_object_or_404, redirect
from booking.forms import BookingForm
from django.contrib.auth.decorators import login_required

from .models import Booking

# Create your views here.
@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()  
            return redirect('index')  
    else:
        form = BookingForm(initial={'booking_date': datetime.date.today()})

    list_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking.html', {'html_form': form, 'html_list': list_bookings})

@login_required
def edit_booking(request):
    return redirect('index') 

@login_required
def delete_booking(request):
    return redirect('index') 
