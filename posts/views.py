from django.shortcuts import render
from comments.forms import CommentForm

# Create your views here.
from comments.models import CommentPost
from posts.forms import PostForm, PostForm2
from posts.models import Post


def listview(request):
    posts = Post.objects.all()

    if request.method == "POST":
        form = PostForm2(data=request.POST)

        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # print(request.user)
        # print(type(request.user))
        # post = Post.objects.create(
        #     title=title,
        #     content=content,
        #     author=request.user
        # )

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

    return render(
        request,
        "posts/list.html",
        {"posts": posts, 'post_form': PostForm2()}
    )


def details(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        print(request.POST)
        if 'post_submit' in request.POST:
            post_form = PostForm2(request.POST, instance=post)
            if post_form.is_valid():
                # post.title = post_form.cleaned_data['title']
                # post.content = post_form.cleaned_data['content']
                # post.save()
                post_form.save()

        elif 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                data = dict(comment_form.cleaned_data)
                data['post'] = post
                comment = CommentPost.objects.create(**data)

    data = {'title': post.title, "content": post.content}
    post_form = PostForm2(data=data)
    comment_form = CommentForm()

    return render(
        request,
        "posts/details.html",
        {"post": post, 'comment_form': comment_form, 'post_form': post_form}
    )
