from django.db import models


class Service(models.Model):
    """
    Represents a service offered by a consultant.

    This class defines a model for a service provided by a consultant.

    **Attributes**
    - `name` : The name of the service. It is a required field and
    cannot be blank.
    - `consultant` : The name of the consultant offering the service.
    It is a required field and cannot be blank.
    """

    name = models.CharField(null=False, blank=False, max_length=50)
    consultant = models.CharField(null=False, blank=False, max_length=50)
