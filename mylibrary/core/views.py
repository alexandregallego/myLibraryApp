from django.shortcuts import render, redirect

# Create your views here.
# Request parameter is info about your browser, IP address, if it is a GET or POST request. Need to be put in all views that we use.

from book.models import Category, Book
from .forms import SignupForm


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


def signup(request):
    # to check if the user has submitted a form
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()  # the user will be created in the database
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })
