from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from blog.form import PostForm
from blog.models import Category, Post


def getAllCategories():
    return Category.objects.all();

def home(request):
    all = getAllCategories()
    posts = Post.objects.all()
    context = {
        'name': 'Leandro Manzano Merlo',
        "languages": all,
        'posts': posts
    }
    return render(request, 'blog/home.html', context);


def show_posts_by_category(request, category_id):
    all_categories = getAllCategories()
    cat = Category.objects.get(pk=category_id)
    if category_id is not None:
        posts = Post.objects.filter(category=cat)
    else:
        posts = Post.objects.all()
    context = {
        'name': 'Leandro Manzano Merlo',
        "languages": all_categories,
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def auth(request):
    error = False
    if request.method == 'POST':
        error = True
        un = request.POST.get('username')
        pd = request.POST.get('password')
        user = authenticate(username=un, password=pd)
        if user is not None:
            error = False
            login(request, user)
    context = {
        'error': error,
    }
    return render(request, 'blog/auth.html', context)

def logout_view(request):
    logout(request)
    return redirect('blog.home')

def post_create(request):
    all_categories = getAllCategories()
    form = PostForm;
    return render(request, 'blog/post_create.html',
    {
        'form': form,
        'languages': all_categories
    })