from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from .forms import BooksForm
from django.core.paginator import Paginator

def book_list(request):
    search = request.GET.get('search', '')
    page = request.GET.get('page', 1)

    books = Books.objects.all()
    if search:
        books = Books.objects.filter(Q(title__icontains=search) | Q(author__icontains=search))
        paginator = Paginator(books, 2)
        books = paginator.get_page(page)
    return render(request, "books/book_list.html", {"books": books, 'search': search})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("books:book_list")
    else:
        form = BooksForm()
    return render(request, "books/book_create.html", {"form": form})

def book_delete(request, id):
    book = get_object_or_404(Books, id=id)
    book.delete()
    return redirect("books:book_list")

def book_update(request, id=None):
    book = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:book_list")
    else:
        form = BooksForm(instance=book)
    return render(request, "books/book_update.html", {"form": form})


# Create your views here.
