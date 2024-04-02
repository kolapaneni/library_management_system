from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .choices import User_Type
from .models import Book, Borrowing
from .serializers import BookSerializer, BorrowingSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        if user.user_type == User_Type.STUDENT:
            queryset = Borrowing.objects.filter(user=user)
        elif user.user_type == User_Type.LIBRARIAN:
            queryset = Borrowing.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
