from django.db import models

from users_app.models import CustomUser

EXIST, NEED = ('exist', 'need')


# Create your models here.
class Book(models.Model):

    BOOK_STATUS = (
        (EXIST, EXIST),
        (NEED, NEED)
    )

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_books'
    )
    status = models.CharField(max_length=10, choices=BOOK_STATUS)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_images/')
    description = models.TextField()

    def __str__(self):
        return self.title
