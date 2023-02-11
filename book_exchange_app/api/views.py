from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, \
    RetrieveDestroyAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from book_exchange_app.api import serializers as exch_serializers
from book_exchange_app.api import permissions as my_permissions
from book_exchange_app import models as exch_models
from book_exchange_app.models import ONGOING
from books_app.models import Book, EXIST, USING


class BookRequestListAPIView(ListCreateAPIView):
    serializer_class = exch_serializers.BookRequestSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return exch_models.BookRequest.objects.filter(for_book__owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)


class BookRequestDetailAPIView(RetrieveDestroyAPIView):
    queryset = exch_models.BookRequest.objects.all()
    serializer_class = exch_serializers.BookRequestSerializer

    permission_classes = [my_permissions.IsSenderOrIsReceiver]


class ResponseToBookRequest(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get objects
        data = request.data
        user = request.user

        book_request = get_object_or_404(exch_models.BookRequest.objects.all(), pk=data.get('book_request'))
        book = get_object_or_404(Book.objects.filter(status=EXIST), pk=data.get('book'))

        # Validations
        if book_request.for_book.owner != user:
            raise PermissionDenied()
        if book.owner != book_request.from_user:
            raise APIException(code=status.HTTP_400_BAD_REQUEST, detail="This book does not belong to requested user!")

        # create Book_Exchange instance
        book_exchange = exch_models.BookExchange(
            book1=book, book2=book_request.for_book, status=ONGOING
        )
        book_exchange.save()

        # Change Books status into USING
        book.change_status(USING)
        book_request.for_book.change_status(USING)

        # Delete Book Request
        book_request.delete()

        # Return information
        serializer = exch_serializers.BookExchangeSerializer(book_exchange)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class BookExchangeListAPIView(ListAPIView):
    queryset = exch_models.BookExchange.objects.all()
    serializer_class = exch_serializers.BookExchangeSerializer

    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status']
    search_fields = ['book1__title', 'book2__title']

    def get_queryset(self):
        user = self.request.user
        return exch_models.BookExchange.objects.filter(
            Q(book1__owner=user) | Q(book2__owner=user)
        ).order_by('-created_at')


class BookExchangeDetailAPIView(RetrieveAPIView):
    queryset = exch_models.BookExchange.objects.all()
    serializer_class = exch_serializers.BookExchangeSerializer

    permission_classes = [my_permissions.IsParticipant]


class EndExchangeRequestListAPIView(ListCreateAPIView):
    serializer_class = exch_serializers.EndExchangeRequestSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return exch_models.EndExchangeRequest.objects.filter(to_user=self.request.user)

    def perform_create(self, serializer):

        serializer.save(from_user=self.request.user)


class EndExchangeRequestDetailAPIView(RetrieveDestroyAPIView):
    queryset = exch_models.EndExchangeRequest.objects.all()
    serializer_class = exch_serializers.EndExchangeRequestSerializer

    permission_classes = [my_permissions.IsOwnerOrReceiverReadOnly]


class ConfirmEndExchangeRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, end_request_id):
        user = self.request.user
        end_request = get_object_or_404(
            exch_models.EndExchangeRequest.objects.filter(),
            id=end_request_id
        )
        pass
