from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from books_app.models import Book, EXIST, NEED
from books_app.api.serializers import BookSerializer
from books_app.api import permissions as books_permissions
from books_app.api.pagination import BookPagination


class BookListAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = BookPagination

    def perform_create(self, serializer):
        status = self.request.query_params.get('status')
        user = self.request.user

        if status.lower() in [EXIST, NEED]:
            serializer.save(status=status, owner=user)
        else:
            raise APIException("Bad Request. Status parameter was not provided!", 400)


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [books_permissions.IsOwnerOrReadOnly]
