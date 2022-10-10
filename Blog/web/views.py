from django.shortcuts import render
from .models import Book
from django.http import HttpResponse


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
    context = {}
    return HttpResponse("<h1>Blog_detail</h1>")