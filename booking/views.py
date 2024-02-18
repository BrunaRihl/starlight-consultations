from django.shortcuts import render


# Create your views here.
def page_booking(request):
    """
    Renders the about page.
    """
    return render(request, "booking.html")
