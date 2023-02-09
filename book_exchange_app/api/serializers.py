from rest_framework import serializers


from book_exchange_app import models as exch_models
from books_app.api.serializers import BookSerializer
from users_app.api.serializers import CustomUserSerializer


class BookRequestSerializer(serializers.ModelSerializer):
    for_book = BookSerializer(read_only=True)
    for_book_id = serializers.IntegerField(write_only=True)

    from_user = CustomUserSerializer(read_only=True)

    class Meta:
        model = exch_models.BookRequest
        fields = ('id', 'for_book', 'for_book_id', 'from_user', 'created_at')
