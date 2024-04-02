from django.urls import path
from .views import AvailableBooks, BorrowBook

urlpatterns = [
    path('available-books/', AvailableBooks.as_view(), name='available_books'),
    path('borrow-book/', BorrowBook.as_view(), name='borrow_book'),
]