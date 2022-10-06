from django.contrib import admin
from .models import Author,Book
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    #exclude = ('name',)
    list_display = ('author_id','name','age','sex')
    list_filter = ('sex',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #exclude = ('name',)
    list_display = ('book_id','name','description','author')
    search_fields = ('name',)
