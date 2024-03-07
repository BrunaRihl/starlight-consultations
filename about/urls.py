from django.urls import path
from . import views

"""
Defines URL patterns for the 'about' app.

This module contains URL patterns for directing requests to the appropriate views
in the 'about' app.

**URL Patterns**
- '' : Directs to the 'about_me' view defined in the 'views' module.
"""

urlpatterns = [
    path('', views.about_me, name='about'),
]
