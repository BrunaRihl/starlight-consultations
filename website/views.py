from django.shortcuts import render

# custom 404 view
def error_404(request, exception):
    return render(request, '404.html', status=404)

# Create your views here.
def page_index(request):
    """
    Renders the index page.
    """
    return render(request, "index.html")
