from rest_framework import serializers
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.generics import get_object_or_404

from book_exchange_app import models as exch_models
from books_app.api.serializers import BookSerializer
from books_app.models import Book, EXIST
from users_app.api.serializers import CustomUserSerializer


class BookRequestSerializer(serializers.ModelSerializer):
    for_book = BookSerializer(read_only=True)
    for_book_id = serializers.IntegerField(write_only=True)

    from_user = CustomUserSerializer(read_only=True)

    class Meta:
        model = exch_models.BookRequest
        fields = ('id', 'for_book', 'for_book_id', 'from_user', 'created_at')
        read_only_fields = ('created_at', )

    def validate(self, data):
        user = self.context['request'].user

        if Book.objects.filter(status=EXIST, id=data['for_book_id']).exclude(owner=user).exists():
            return data
        raise ValidationError({
            'for_book_id': 'Book does not exist with given ID'
        })


class BookExchangeSerializer(serializers.ModelSerializer):
    book1 = BookSerializer(read_only=True)
    book2 = BookSerializer(read_only=True)

    class Meta:
        model = exch_models.BookExchange
        fields = ('id', 'book1', 'book2', 'status', 'created_at')
        read_only_fields = ('status', 'created_at')


class EndExchangeRequestSerializer(serializers.ModelSerializer):
    exchange = BookExchangeSerializer(read_only=True)
    exchange_id = serializers.IntegerField(write_only=True)

    from_user = CustomUserSerializer(read_only=True)

    class Meta:
        model = exch_models.EndExchangeRequest
        fields = ('id', 'exchange', 'exchange_id', 'from_user', 'created_at')
        read_only_fields = ('created_at', )

    def validate(self, data):
        user = self.context['request'].user

        book_exchange = get_object_or_404(
            exch_models.BookExchange.objects.filter(status=exch_models.ONGOING), id=data['exchange_id']
        )
        if not book_exchange.is_participant(user):
            raise PermissionDenied()

        if book_exchange.book1.owner == user:
            to_user = book_exchange.book2.owner
        else:
            to_user = book_exchange.book1.owner

        data['to_user_id'] = to_user.id

        return data
