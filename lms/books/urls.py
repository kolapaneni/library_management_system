from django.urls import path, include

from books.utils import NoPutRouter
from books.views import BookViewSet, BorrowingViewSet

router = NoPutRouter()

router.register(r'books', BookViewSet, basename="book")
router.register(r'borrowings', BorrowingViewSet, basename="borrowings")

urlpatterns = [
    path('', include(router.urls)),
]
