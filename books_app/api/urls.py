from django.urls import path

from books_app.api import views as books_views

app_name = 'books'

urlpatterns = [
    path('', books_views.BookListAPIView.as_view(), name='books-list'),
    path('<int:pk>/', books_views.BookDetailAPIView.as_view(), name='book-detail'),

]
