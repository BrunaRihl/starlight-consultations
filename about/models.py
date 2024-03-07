from django.db import models
from cloudinary.models import CloudinaryField

class About(models.Model):
    """
    Model representing information about the website.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        """
        String for representing the About object.
        """
        return self.title
