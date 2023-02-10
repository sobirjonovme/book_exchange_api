from django.db import models
from django.utils import timezone

from users_app.models import CustomUser
from books_app.models import Book

ONGOING, END = ('ongoing', 'end')
BOOK_EXCHANGE_STATUS = (
    (ONGOING, ONGOING),
    (END, END)
)


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
        related_name='book_requests_from_user'
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"for {self.for_book.title} from {self.from_user.username}"


class BookExchange(models.Model):
    book1 = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_exchanges_1'
    )
    book2 = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_exchanges_2'
    )
    status = models.CharField(max_length=10, choices=BOOK_EXCHANGE_STATUS, default=ONGOING)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.book1.title} | {self.book1.owner.username}  AND  {self.book2.title} | {self.book2.owner.username}"


class EndExchangeRequest(models.Model):
    exchange = models.ForeignKey(
        BookExchange,
        on_delete=models.CASCADE,
        related_name='end_exchange_requests'
    )
    from_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='end_exchange_requests_from_user'
    )
    to_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='end_exchange_requests_to_user'
    )
