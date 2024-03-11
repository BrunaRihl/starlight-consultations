from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About


# Register the About model with SummernoteModelAdmin
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin class for managing the About model.

    This class uses SummernoteModelAdmin to provide a rich text editor
    for the 'content' field of the About model.
    """

    summernote_fields = ("content",)
