from django.shortcuts import render

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
