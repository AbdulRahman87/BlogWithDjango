from django.shortcuts import render
from . models import Post
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    blogPosts = Post.objects.all().order_by('date_of_creation').reverse()
    paginator = Paginator(blogPosts, 4)
    page_number = request.GET.get('page_no')
    posts = paginator.get_page(page_number)
    context = {'posts': posts}
    return render(request, 'index.html', context)

def blogPost(request, title, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'content.html', context)