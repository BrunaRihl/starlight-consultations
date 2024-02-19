from django import forms
from booking.models import Booking
from service.models import Service

TIME_OPTIONS = [(f"{hour}:00", f"{hour}:00") for hour in range(9, 18)]
SERVICE_OPTIONS = Service.objects.all()

class BookingForm(forms.ModelForm):
    services = forms.ChoiceField(
        required=True,
        choices=SERVICE_OPTIONS,
        widget=forms.Select(attrs={"class": "form-control"}),
    )


    booking_time = forms.ChoiceField(
        required=True,
        choices=TIME_OPTIONS,
        widget=forms.Select(attrs={"class": "form-control"}),
    )


    booking_date = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={"class": "form-control datepicker", "type": "date"}
        ),
    )
   
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": "3",
                "class": "form-control",
                "placeholder": "Message here...",
            }
        ),
    )
   
    class Meta:
        model = Booking
        fields = ["service", "booking_date", "booking_time", "message"]
        widgets = {
            "user": forms.HiddenInput(), 
        }
