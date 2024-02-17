from django.shortcuts import render


# Create your views here.
def page_index(request):
    """
    Renders the about page.
    """
    return render(request, "pages/index.html")
