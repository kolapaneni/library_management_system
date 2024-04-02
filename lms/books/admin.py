from django.contrib import admin

from books.models import Borrowing, Book

admin.site.register(Book)
admin.site.register(Borrowing)
