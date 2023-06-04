from django.shortcuts import render

# Create your views here.
# Request parameter is info about your browser, IP address, if it is a GET or POST request. Need to be put in all views that we use.

from book.models import Category, Book


def index(request):
    # to show the firts six books
    books = Book.objects.all()[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
                  'categories': categories,
                  'books': books
                  })


def contact(request):
    return render(request, 'core/contact.html')
