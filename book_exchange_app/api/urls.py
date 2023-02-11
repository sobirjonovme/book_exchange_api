from django.urls import path

from book_exchange_app.api import views as exch_views


app_name = 'book_exchange_app'

urlpatterns = [
    path('', exch_views.BookExchangeListAPIView.as_view(), name='book-exchange-list'),
    path('<int:pk>/', exch_views.BookExchangeDetailAPIView.as_view(), name='book-exchange-detail'),

    path('book-requests/', exch_views.BookRequestListAPIView.as_view(), name='book-request-list'),
    path('book-requests/<int:pk>/', exch_views.BookRequestDetailAPIView.as_view(), name='book-request-detail'),

    path('response-to-book-request/', exch_views.ResponseToBookRequest.as_view(), name='response-to-book-request'),

    path('end-book-exchange-requests/', exch_views.EndExchangeRequestListAPIView.as_view(),
         name='end-exchange-request-list'),
    path('end-book-exchange-requests/<int:pk>/', exch_views.EndExchangeRequestDetailAPIView.as_view(),
         name='end-exchange-request-detail'),

    path('confirm-end-exchange-request/<int:end_request_id>/', exch_views.ConfirmEndExchangeRequestAPIView.as_view(),
         name='confirm-end-exchange-request'),

]
