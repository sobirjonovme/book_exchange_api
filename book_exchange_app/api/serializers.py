from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
        print(user)
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
