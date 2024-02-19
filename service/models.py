from django.db import models

# Create your models here.
class Service(models.Model):
   name = models.CharField(null=False, blank=False,  max_length=50)
   consultant = models.CharField(null=False, blank=False, max_length=50)