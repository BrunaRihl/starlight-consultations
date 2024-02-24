import datetime

from django.shortcuts import render, get_object_or_404, redirect
from booking.forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Booking

# Create your views here.
@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()  
            messages.success(request, "Booking saved successful")
            return redirect('create_booking')  
    else:
        form = BookingForm(initial={'booking_date': datetime.date.today()})

    list_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking.html', {'html_form': form, 'html_list': list_bookings})

@login_required
def edit_booking(request, booking_id):
    # get booking object
    print("booking_id", booking_id)
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == "POST":
        # create booking form
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successful")
            return redirect("create_booking")

        else:
            messages.error(request, "Ops... Something goes wrong")
    else:
        # create a booking instance
        form = BookingForm(instance=booking)

    return render(
        request,
        "edit_booking.html",
        {"html_form": form, 
         "booking_id": booking_id},
    )


@login_required
def delete_booking(request, booking_id):
    """
    For deleting booking
    """
    # Recupera a instância da reserva
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == 'POST':
        # Remove a reserva
        booking.delete()
        # success message
        messages.success(request, "Booking deleted successful")
        # Redireciona para algum lugar apropriado após a remoção
        return redirect('create_booking')

    # Carrega o formulário preenchido com os dados da reserva
    form = BookingForm(instance=booking, readonly=True)

    return render(request, 'delete_booking.html', {'form': form, 'booking_id': booking_id})