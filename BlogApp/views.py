from django.shortcuts import render, redirect
from .models import Blog
from .forms import CommentForm

# Create your views here.
def home(request):
    list = Blog.objects.all().order_by('-id')
    return render(request, 'home.html', { 'listBlog': list })

def blog(request, id):
    postItem = Blog.objects.get(id = id)
    form = CommentForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'blog.html', { 'post': postItem, 'form': form })