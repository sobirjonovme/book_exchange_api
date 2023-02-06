from rest_framework.generics import ListCreateAPIView
from rest_framework.exceptions import APIException

from books_app.models import Book, EXIST, NEED
from books_app.api import serializers as books_serializers


class BookListAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = books_serializers.BookSerializer

    def perform_create(self, serializer):
        status = self.request.query_params.get('status')
        user = self.request.user

        if status.lower() in [EXIST, NEED]:
            serializer.save(status=status, owner=user)
        else:
            raise APIException("Bad Request. Status parameter was not provided!", 400)
