from django_filters import rest_framework as filters
from rest_framework.exceptions import AuthenticationFailed

from books_app.models import Book, BOOK_STATUS, EXIST, NEED
from users_app.models import CustomUser


class BookFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=BOOK_STATUS)
    owner = filters.CharFilter(field_name='owner__username', method='owner_filter', lookup_expr='iexact')
    match = filters.BooleanFilter(field_name='is_match', method='is_match_filter')

    class Meta:
        model = Book
        fields = ('owner', 'status', 'match')

    def owner_filter(self, queryset, name, value):
        if value == 'self':
            value = self.request.user.username

        return queryset.filter(owner__username=value)

    def is_match_filter(self, queryset, name, value):

        if self.request.user.is_authenticated is False:
            raise AuthenticationFailed("Authentication credentials were not provided.")

        if value is True:
            current_user = self.request.user
            current_user_need_books = current_user.user_books.filter(status=NEED)
            current_user_existing_books = current_user.user_books.filter(status=EXIST)

            need_me_users = []
            users = CustomUser.objects.all()

            for user in users:
                user_need_books = user.user_books.filter(status=NEED)
                if current_user_existing_books.filter(title__in=[book.title for book in user_need_books]).exists():
                    need_me_users.append(user.id)
            # print(need_me_users)

            return Book.objects.filter(
                owner__id__in=need_me_users,
                title__in=[book.title for book in current_user_need_books]
            )

        return queryset
