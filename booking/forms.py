from datetime import datetime
from django import forms
from booking.models import Booking
from service.models import Service
from django.core.exceptions import ValidationError
from datetime import date



TIME_OPTIONS = [(f"{hour}:00", f"{hour}:00") for hour in range(9, 18)]
SERVICE_OPTIONS = [(service.id, service.name) for service in Service.objects.all()]
current_date = date.today()


class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        readonly = kwargs.pop('readonly', False)
        super(BookingForm, self).__init__(*args, **kwargs)
        if readonly:
            for field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True
                self.fields[field_name].widget.attrs['disabled'] = True

    service = forms.ChoiceField(
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
            attrs={"class": "form-control datepicker", "type": "date", "min": current_date}
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

    def clean_service(self):
        service_id = self.cleaned_data['service']
        try:
            service = Service.objects.get(pk=service_id)
            return service
        except Service.DoesNotExist:
            raise forms.ValidationError("Selected service not valid.")
        


    def clean(self):
        """
        """
        current_date = datetime.now().date()
        current_time = datetime.now().time()

        cleaned_data = super().clean()
        booking_date = cleaned_data.get("booking_date")
        booking_time = datetime.strptime(
            cleaned_data.get("booking_time"), "%H:%M"
        ).time()

        if booking_date <= current_date and booking_time <= current_time:
            raise ValidationError("Please select a valid date for the booking, which should be later than today.")

        if Booking.objects.filter(
            booking_date=booking_date,
            booking_time=cleaned_data.get("booking_time"),
        ).exists():
            raise ValidationError("Consultant is not available on this day/time.")

    