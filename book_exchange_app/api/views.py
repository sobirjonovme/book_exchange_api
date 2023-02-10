from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, APIException

from book_exchange_app.api import serializers as exch_serializers
from book_exchange_app import models as exch_models
from book_exchange_app.models import ONGOING
from books_app.models import Book, EXIST


class BookRequestListAPIView(ListCreateAPIView):
    queryset = exch_models.BookRequest.objects.all().order_by('-created_at')
    serializer_class = exch_serializers.BookRequestSerializer


class ResponseToBookRequest(APIView):
    def post(self, request):
        data = request.data
        user = request.user
        print(data)

        book_request = get_object_or_404(exch_models.BookRequest.objects.all(), pk=data.get('book_request'))
        book = get_object_or_404(Book.objects.filter(status=EXIST), pk=data.get('book'))

        print(book_request.for_book.owner)
        print(user)
        if book_request.for_book.owner != user:
            raise PermissionDenied()

        if book.owner != book_request.from_user:
            raise APIException(code=status.HTTP_400_BAD_REQUEST, detail="This book does not belong to requested user!")

        book_exchange = exch_models.BookExchange(
            book1=book, book2=book_request.for_book, status=ONGOING
        )
        book_exchange.save()

        print("\n\na\n\n")
        return Response(status=200)
