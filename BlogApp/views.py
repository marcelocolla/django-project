from django.shortcuts import render, redirect
from .models import Blog, Comentario
from .forms import CommentForm

# Create your views here.
def home(request):
    list = Blog.objects.all().order_by('-id')
    return render(request, 'home.html', { 'listBlog': list })

def blog(request, id):
    post = Blog.objects.get(id = id)
    listComments = Comentario.objects.filter(blog = post)
    form = CommentForm(request.POST or None)
    
    if form.is_valid():
        addComment = form.save(commit=False)
        addComment.blog_id = post.id
        addComment.save()
        return redirect('blog', post.id)

    return render(request, 'blog.html', { 'post': post, 'listComments': listComments, 'form': form })