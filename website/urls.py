from django.urls import path
from . import views
from .views import page_index


urlpatterns = [
    path("", page_index, name="index"),

]
