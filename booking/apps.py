from django.apps import AppConfig


class BookingConfig(AppConfig):
    """
    Configures the booking app.

    Attributes:
    default_auto_field (str): Sets the default auto-generated
    field for primary keys.
    name (str): Defines the name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "booking"
