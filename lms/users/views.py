from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from books.models import Book, Borrowing
from books.serializers import BookSerializer, BorrowingSerializer


class AvailableBooks(APIView):

    def get(self, request, *args, **kwargs):
        available_books = Book.objects.filter(copies_available__gt=0)
        serializer = BookSerializer(available_books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BorrowBook(APIView):
    def post(self, request):
        book_id = request.data.get('book_id')
        user_id = request.user.id
        book = Book.objects.get(pk=book_id)

        if book.copies_available <= 0:
            return Response({"message": "No available copies of this book."}, status=status.HTTP_400_BAD_REQUEST)

        if Borrowing.objects.filter(user_id=user_id, book_id=book_id).exists():
            return Response({"message": "You have already borrowed this book."}, status=status.HTTP_400_BAD_REQUEST)

        borrowing = Borrowing.objects.create(user_id=user_id, book_id=book_id)
        book.copies_available -= 1
        book.save()
        serializer = BorrowingSerializer(borrowing)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
