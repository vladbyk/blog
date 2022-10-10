from django.shortcuts import render
from .models import Book


def HomeView(request):
    return render(request, 'home/home.html')


def ContactsView(request):
    return render(request, 'contacts/contacts.html')


def BlogView(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'blog/blogs.html', context)

def Blog_detailView(request,num):
    print(num)
    context = {
        'books': Book.objects.filter(book_id=num)
    }
    return render(request, 'blog/detail_blog.html', context)