from rest_framework.generics import CreateAPIView

from books_app.models import Book, EXIST, NEED
from books_app.api import serializers as books_serializers


class BookListAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = books_serializers.BookSerializer

    def perform_create(self, serializer):
        status = self.kwargs.get('status')
        user = self.request.user

        if status in [EXIST, NEED]:
            serializer.save(status=status, owner=user)
