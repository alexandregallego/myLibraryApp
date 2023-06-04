from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import NewBookForm

# Create your views here.


def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    related_books = Book.objects.filter(
        category=book.category).exclude(pk=pk)
    return render(request, 'book/detail.html', {
        'book': book,
        'related_books': related_books
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES)

        if form.is_valid():
            # If you try to save to the database now, the created_by field is not added. Therefore we will get an error and set commit=False
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()

            return redirect('book:detail', pk=book.id)
    else:
        form = NewBookForm()

    return render(request, 'book/form.html', {
        'form': form,
        'book': 'New book',
    })
