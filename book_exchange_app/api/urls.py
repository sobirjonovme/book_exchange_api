from django.urls import path

from book_exchange_app.api import views as exch_views


app_name = 'book_exchange_app'

urlpatterns = [
    path('', exch_views.BookExchangeListAPIView.as_view(), name='book-exchange-list'),
    path('<int:pk>/', exch_views.BookExchangeDetailAPIView.as_view(), name='book-exchange-detail'),

    path('book-requests/', exch_views.BookRequestListAPIView.as_view(), name='book-request-list'),
    path('book-requests/<int:pk>/', exch_views.BookRequestDetailAPIView.as_view(), name='book-request-detail'),
    path('book-requests/<int:book_request_id>/response/',
         exch_views.ResponseToBookRequest.as_view(), name='response-to-book-request'),

    path('end-exchange-requests/',
         exch_views.EndExchangeRequestListAPIView.as_view(), name='end-exchange-request-list'),
    path('end-exchange-requests/<int:pk>/',
         exch_views.EndExchangeRequestDetailAPIView.as_view(), name='end-exchange-request-detail'),
    path('end-exchange-requests/<int:end_request_id>/confirm/',
         exch_views.ConfirmEndExchangeRequestAPIView.as_view(), name='confirm-end-exchange-request'),

]
