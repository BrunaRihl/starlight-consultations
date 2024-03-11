from datetime import date
from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from booking.models import Booking
from service.models import Service


# Generate time options for booking
TIME_OPTIONS = [(f"{hour}:00", f"{hour}:00") for hour in range(9, 18)]

# Generate service options for booking
SERVICE_OPTIONS = [
    (service.id, service.name) for service in Service.objects.all()
]

# Get the current date
current_date = date.today()


class BookingForm(forms.ModelForm):
    """
    Form for booking a service.

    This form provides fields for selecting a service, booking date and time,
    and leaving an optional message.

    **Attributes**
    service: ChoiceField: Field for selecting a service.
    booking_time: ChoiceField: Field for selecting a booking time.
    booking_date: DateField: Field for selecting a booking date.
    message: CharField: Field for leaving an optional message.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the form instance.

        Parameters:
        *args: Positional arguments.
        **kwargs: Keyword arguments.
        """
        readonly = kwargs.pop("readonly", False)
        super(BookingForm, self).__init__(*args, **kwargs)
        if readonly:
            # Set fields as read-only if specified
            for field_name in self.fields:
                self.fields[field_name].widget.attrs["readonly"] = True
                self.fields[field_name].widget.attrs["disabled"] = True

    # Define ChoiceField for selecting a service
    service = forms.ChoiceField(
        required=True,
        choices=SERVICE_OPTIONS,  # Set choices for the service field
        widget=forms.Select(
            attrs={"class": "form-control"}
        ),  # Set widget attributes for styling
    )

    # Define ChoiceField for selecting booking time
    booking_time = forms.ChoiceField(
        required=True,
        choices=TIME_OPTIONS,  # Set choices for the booking time field
        widget=forms.Select(
            attrs={"class": "form-control"}
        ),  # Set widget attributes for styling
    )

    # Define DateField for selecting booking date
    booking_date = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                "class": "form-control datepicker",
                "type": "date",
                "min": current_date,
            }  # Set widget attributes for styling and minimum date
        ),
    )

    # Define CharField for entering an optional message
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": "3",  # Set number of rows for the textarea
                "class": "form-control",  # Set CSS class for styling
                "placeholder": "Message here...",  # Set placeholder text
            }
        ),
    )

    class Meta:
        model = Booking  # Set the model associated with the form
        fields = [
            "service",
            "booking_date",
            "booking_time",
            "message",
        ]  # Specify fields to be included in the form
        widgets = {
            "user": forms.HiddenInput(),  # Hide the user field in the form
        }

    def clean_service(self):
        """
        Validates the selected service.

        Returns:
        service: The selected service.

        ValidationError: If the selected service is not valid.
        """
        service_id = self.cleaned_data["service"]
        try:
            # Check if the selected service exists
            service = Service.objects.get(pk=service_id)
            return service
        except Service.DoesNotExist:
            raise forms.ValidationError("Selected service not valid.")

    def clean(self):
        """
        Validates the booking date and time.

        ValidationError: If the booking date and time are not valid.
        """
        current_date = datetime.now().date()
        current_time = datetime.now().time()

        cleaned_data = super().clean()
        booking_date = cleaned_data.get("booking_date")
        booking_time = datetime.strptime(
            cleaned_data.get("booking_time"), "%H:%M"
        ).time()

        if booking_date <= current_date and booking_time <= current_time:
            # Check if the booking date and time are valid
            raise ValidationError(
                "Please select a valid date for the booking, "
                "which should be later than today."
            )

        if Booking.objects.filter(
            booking_date=booking_date,
            booking_time=cleaned_data.get("booking_time"),
        ).exists():
            # Check if the consultant is available on the selected date and time
            raise ValidationError(
                "Consultant is not available on this day/time."
            )
