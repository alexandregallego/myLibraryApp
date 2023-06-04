from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.


def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    related_books = Book.objects.filter(
        category=book.category).exclude(pk=pk)
    return render(request, 'book/detail.html', {
        'book': book,
        'related_books': related_books
    })
