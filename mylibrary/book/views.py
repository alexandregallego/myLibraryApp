from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Book, Category
from .forms import NewBookForm, EditBookForm

# Create your views here.


def books(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    books = Book.objects.all()

    if category_id:
        books = books.filter(category_id=category_id)

    if query:
        books = books.filter(Q(name__icontains=query) |
                             Q(description__icontains=query))

    return render(request, 'book/books.html', {
        'books': books,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })


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


@login_required
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk, created_by=request.user)
    book.delete()
    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    book = get_object_or_404(Book, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            # If you try to save to the database now, the created_by field is not added. Therefore we will get an error and set commit=False
            form.save()

            return redirect('book:detail', pk=book.id)
    else:
        form = EditBookForm(instance=book)

    return render(request, 'book/form.html', {
        'form': form,
        'book': 'Edit book',
    })
