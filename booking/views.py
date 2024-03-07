import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from booking.forms import BookingForm
from .models import Booking

@login_required
def create_booking(request):
    """
    View function for creating a new booking.
    If the request method is POST, validates the form and saves the booking.
    Otherwise, displays the booking form with today's date as initial value.
    **Context**
    ``html_form``
        The HTML form for creating a new booking.
    ``html_list``
        The list of bookings associated with the current user.
    **Template**
    :template:`booking.html`
    """
    if request.method == 'POST':
        # Validate and save the form if it's a POST request
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()  
            messages.success(request, "Booking saved successful")
            return redirect('create_booking')  
    else:
        # Display the form with today's date as initial value
        form = BookingForm(initial={'booking_date': datetime.date.today()})

    # Get the list of bookings associated with the current user
    list_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking.html', {'html_form': form, 'html_list': list_bookings})

@login_required
def edit_booking(request, booking_id):
    """
    View function for editing an existing booking.

    Retrieves the booking object and populates the form with its data.
    If the request method is POST, validates the form and updates the booking.

    **Context**
    ``html_form``
        The HTML form for editing the booking.
    ``booking_id``
        The ID of the booking being edited.

    **Template**
    :template:`edit_booking.html`
    """
    # Retrieve the booking object
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == "POST":
        # Create a form instance with the booking data
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successful")
            return redirect("create_booking")
        else:
            messages.error(request, "Ops... Something goes wrong")
    else:
        # Create a form instance with the booking data
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
    View function for deleting a booking.

    Retrieves the booking object and renders the delete confirmation form.
    If the request method is POST, deletes the booking.

    **Context**
    ``form``
        The form pre-filled with booking data.
    ``booking_id``
        The ID of the booking being deleted.

    **Template**
    :template:`delete_booking.html`
    """
    # Retrieve the booking object
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == 'POST':
        # Delete the booking if it's a POST request
        booking.delete()
        messages.success(request, "Booking deleted successful")
        return redirect('create_booking')

    # Create a form instance with the booking data
    form = BookingForm(instance=booking, readonly=True)

    return render(request, 'delete_booking.html', {'form': form, 'booking_id': booking_id})




