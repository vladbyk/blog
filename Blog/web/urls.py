from django.urls import path
from .views import ContactsView,HomeView,BlogView

urlpatterns = [
    path("",HomeView,name="base"),
    path("contacts/",ContactsView, name="contacts"),
    path("blogs/",BlogView, name="blogs"),
]
