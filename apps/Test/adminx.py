import xadmin
from xadmin import views

from .models import Book, Author


class BookAdmin:
    list_display = ['name']


class AuthorAdmin:
    list_dispaly = ['name']


xadmin.site.register(Book, BookAdmin)
xadmin.site.register(Author, AuthorAdmin)
