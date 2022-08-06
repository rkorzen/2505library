from django.shortcuts import render

from books.models import Book


def list(request):
    books = Book.objects.all()
    return render(
        request,
        "books/list.html",
        {"books": books}
    )


def details(request, book_id):
    book = Book.objects.get(pk=book_id)

    return render(
        request,
        "books/details.html",
        {"book": book}
    )
