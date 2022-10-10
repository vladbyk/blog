from django.urls import path
from .views import ContactsView,HomeView,BlogView,Blog_detailView

urlpatterns = [
    path("",HomeView,name="base"),
    path("contacts/",ContactsView, name="contacts"),
    path("blogs/",BlogView, name="blogs"),
    path("blogs/<int:num>",Blog_detailView, name="blog_detail"),
]
