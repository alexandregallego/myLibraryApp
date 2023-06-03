from django.shortcuts import render

# Create your views here.
# Request parameter is info about your browser, IP address, if it is a GET or POST request. Need to be put in all views that we use.


def index(request):
    return render(request, 'core/index.html')
