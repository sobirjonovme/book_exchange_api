from rest_framework import serializers

from users_app.api.serializers import CustomUserSerializer
from books_app.models import Book


class BookSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'owner', 'status', 'title', 'author', 'image', 'description')
        read_only_fields = ('status', )
