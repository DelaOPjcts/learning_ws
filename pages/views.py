from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("Homepage")

def about_page_view(request):
    #return render(request, "pages/about.html")
    context = {"name": "Daniel",
               "age": 37}
    return render(request, "pages/about.html", context)