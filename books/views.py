from django.shortcuts import render, redirect
from .models import Books


def list_books(request):
    all_books = Books.objects.all()
    return render(request, 'books/all_books.html', {'all_books': all_books})

def retrieve_single_book(request, id_from_the_web):
    book = Books.objects.get(id=id_from_the_web)
    return render(request, 'books/single_books.html', {'book': book})

def delete_book(request, id_from_the_web):
    book = Books.objects.get(id=id_from_the_web)
    book.delete()
    return redirect("list-all-books")

# def update_book(request, id_from_the_web):
#     book = Books.objects.get(id=id_from_the_web)
#     if request.method == 'POST':