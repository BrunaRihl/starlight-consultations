from django.urls import path
from .views import page_index


urlpatterns = [
    # URL pattern for the index page
    path("", page_index, name="index"),
]
