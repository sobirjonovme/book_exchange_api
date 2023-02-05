from django.urls import path

from books_app.api import views as books_views

app_name = 'books'

urlpatterns = [
    path('add/<str:status>/', books_views.BookListAPIView.as_view(), name='books-list'),
]
