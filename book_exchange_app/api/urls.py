from django.urls import path

from book_exchange_app.api import views as exch_views


app_name = 'book_exchange_app'

urlpatterns = [
    path('book-requests/', exch_views.BookRequestListAPIView.as_view(), name='book-requests'),

]
