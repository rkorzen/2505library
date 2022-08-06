from django.shortcuts import render

# Create your views here.
from authors.models import Author


def list(request):
    authors = Author.objects.all()
    return render(
        request,
        "authors/list.html",
        {"authors": authors}
    )



def details(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(
        request,
        "authors/details.html",
        {"author": author}
    )
