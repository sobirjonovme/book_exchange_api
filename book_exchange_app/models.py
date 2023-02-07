from django.db import models
from django.utils import timezone


from users_app.models import CustomUser
from books_app.models import Book


# Create your models here.
class BookRequest(models.Model):
    for_book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='requests_for_book'
    )
    from_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='requests_from_user'
    )
    created_at = models.DateTimeField(default=timezone.now)
