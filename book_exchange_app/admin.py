from django.contrib import admin

from book_exchange_app import models as exchange_models


# Register your models here.
admin.site.register(exchange_models.BookRequest)
admin.site.register(exchange_models.BookExchange)
admin.site.register(exchange_models.EndExchangeRequest)
