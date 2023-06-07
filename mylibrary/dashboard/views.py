from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from book.models import Book


@login_required
def index(request):
    books = Book.objects.filter(created_by=request.user)
    return render(request, 'dashboard/index.html', {
        'books': books,
    })
