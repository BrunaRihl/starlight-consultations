from django import forms
from booking.models import Booking
from service.models import Service

TIME_OPTIONS = [(f"{hour}:00", f"{hour}:00") for hour in range(9, 18)]
SERVICE_OPTIONS = [(service.id, service.name) for service in Service.objects.all()]


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

    def clean_service(self):
        service_id = self.cleaned_data['service']
        try:
            service = Service.objects.get(pk=service_id)
            return service
        except Service.DoesNotExist:
            raise forms.ValidationError("Serviço selecionado não existe.")