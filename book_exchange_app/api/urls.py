from django.urls import path

from book_exchange_app.api import views as exch_views


app_name = 'book_exchange_app'

urlpatterns = [
    path('book-requests/', exch_views.BookRequestListAPIView.as_view(), name='book-requests'),
    path('response-to-book-request/', exch_views.ResponseToBookRequest.as_view(), name='response-to-book-request'),

]
