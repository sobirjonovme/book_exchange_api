from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, APIException
from rest_framework.permissions import IsAuthenticated

from book_exchange_app.api import serializers as exch_serializers
from book_exchange_app import models as exch_models
from book_exchange_app.models import ONGOING
from books_app.models import Book, EXIST


class BookRequestListAPIView(ListCreateAPIView):
    serializer_class = exch_serializers.BookRequestSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return exch_models.BookRequest.objects.filter(for_book__owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)


class ResponseToBookRequest(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user

        book_request = get_object_or_404(exch_models.BookRequest.objects.all(), pk=data.get('book_request'))
        book = get_object_or_404(Book.objects.filter(status=EXIST), pk=data.get('book'))

        if book_request.for_book.owner != user:
            raise PermissionDenied()

        if book.owner != book_request.from_user:
            raise APIException(code=status.HTTP_400_BAD_REQUEST, detail="This book does not belong to requested user!")

        book_exchange = exch_models.BookExchange(
            book1=book, book2=book_request.for_book, status=ONGOING
        )
        book_exchange.save()

        serializer = exch_serializers.BookExchangeSerializer(book_exchange)

        return Response(data=serializer.data, status=200)
