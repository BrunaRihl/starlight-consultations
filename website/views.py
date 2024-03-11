from django.shortcuts import render


# Custom 404 view
def error_404(request, exception):
    """
    View function for rendering the custom 404 error page.

    **Template**
    :template:`404.html`
    """
    return render(request, "404.html", status=404)


# Index page view
def page_index(request):
    """
    View function for rendering the index page.

    **Template**
    :template:`index.html`
    """
    return render(request, "index.html")
