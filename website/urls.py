from . import views
from django.urls import path


urlpatterns = [
    path("", page_index, name="index"),

]
