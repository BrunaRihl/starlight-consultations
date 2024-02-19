from django.shortcuts import render, redirect
from booking.forms import BookingForm
from django.contrib.auth.decorators import login_required

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
        form = BookingForm()
    return render(request, 'booking.html', {'html_form': form})

