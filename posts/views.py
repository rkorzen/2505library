from django.shortcuts import render

# Create your views here.
from posts.models import Post


def listview(request):
    posts = Post.objects.all()
    print(request.method)
    print(request.user)
    print(request.user.is_authenticated)
    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")
        print(request.user)
        print(type(request.user))
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )

    return render(
        request,
        "posts/list.html",
        {"posts": posts,

         "x": "123",
         "y": "ccdcdc",
         }
    )

def details(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")

        post.title = title
        post.content = content

        post.save()

    return render(
        request,
        "posts/details.html",
        {"post": post,}
    )