from django.contrib import admin

from book_exchange_app import models as exchange_models


class BookExchangeAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'status')
    list_filter = ('status', )


# Register your models here.
admin.site.register(exchange_models.BookRequest)
admin.site.register(exchange_models.BookExchange, BookExchangeAdmin)
admin.site.register(exchange_models.EndExchangeRequest)
