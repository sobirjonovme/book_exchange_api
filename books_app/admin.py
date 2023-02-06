from django.contrib import admin

from books_app.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'status', 'owner')
    list_filter = ('status', )


# Register your models here.
admin.site.register(Book, BookAdmin)
