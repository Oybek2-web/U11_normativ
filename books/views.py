from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from .forms import BooksForm

def book_list(request):
    books = Books.objects.all()
    return render(request, "books/book_list.html", {"books": books})

def book_create(request):
    if request.method == 'POST':
        forms = BooksForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("books:book_list")
        return render(request, "books/book_create.html", {"form": forms})
    forms = BooksForm()
    return render(request, "books/book_create.html", {"form": forms})

def book_delete(request, id):
    book = get_object_or_404(Books, id=id)
    book.delete()
    return redirect("books:book_list")

def book_update(request, id=None):
    book = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        forms = BooksForm(request.POST, instance=book)
        if forms.is_valid():
            forms.save()
            return redirect("books:book_list")
        return render(request, "books/book_update.html", {"form": forms})
    forms = BooksForm(instance=book)
    return render(request, "books/book_update.html", {"form": forms})


# Create your views here.
