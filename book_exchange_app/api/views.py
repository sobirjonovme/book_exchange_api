from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView

from book_exchange_app.api import serializers as exch_serializers
from book_exchange_app import models as exch_models


class BookRequestListAPIView(ListCreateAPIView):
    queryset = exch_models.BookRequest.objects.all().order_by('-created_at')
    serializer_class = exch_serializers.BookRequestSerializer


class ResponseToBookRequest(APIView):
    def post(self, request):
        pass