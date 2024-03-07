from django.apps import AppConfig


class ServiceConfig(AppConfig):
    """
    Configures the Service app for Django.
    
    **Attributes**
    - `default_auto_field` : Specifies the default primary key field for models in the Service app.
    - `name` : Specifies the name of the Service app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service'
