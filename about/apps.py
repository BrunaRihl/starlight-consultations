from django.apps import AppConfig


# Configuration class for the 'about' app
class AboutConfig(AppConfig):
    """
    Configuration class for the 'about' app.

    This class defines the configuration settings for the 'about' app,
    including the default auto field and the app name.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "about"
