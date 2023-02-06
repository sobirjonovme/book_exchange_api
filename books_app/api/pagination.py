from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BookPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': super().get_next_link(),
                'previous': super().get_previous_link()
            },
            'total_elements': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page': super().get_page_number(self.request, self.page.paginator),
            'results': data
        })
