from django.shortcuts import render
from .models import About

# Create your views here.


def about_me(request):
    """
    Renders the about page, displaying the most recent information.
    
    Retrieves the latest instance of :model:`about.About`.
    
    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
        
    **Template**
    :template:`about/about.html`
    """

    # Get the latest About object
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about.html",
        {"about": about},
    )

