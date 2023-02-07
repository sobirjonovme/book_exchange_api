from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from books_app.models import Book, EXIST, NEED
from books_app.api.serializers import BookSerializer
from books_app.api import permissions as books_permissions
from books_app.api.pagination import BookPagination
from books_app.api.filters import BookFilter


class BookListAPIView(ListCreateAPIView):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = BookPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']

    def perform_create(self, serializer):
        book_status = self.request.query_params.get('status')
        user = self.request.user

        if book_status is not None and book_status.lower() in [EXIST, NEED]:
            serializer.save(status=book_status, owner=user)
        else:
            raise APIException("Bad Request. Status parameter was not provided!", status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [books_permissions.IsOwnerOrReadOnly]
