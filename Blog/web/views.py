from django.shortcuts import render
from django.http import HttpResponse

def HomeView(request):
    return render(request,'home/home.html')


def ContactsView(request):
    return render(request,'contacts/contacts.html')

def BlogView(request):
    return render(request,'blog/blogs.html')