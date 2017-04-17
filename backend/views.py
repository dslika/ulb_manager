from rest_framework import viewsets

from backend.models import Staff
from backend.models import Stock
from backend.serializer import StockSerializer


# Create your views here.
# RestAPIのview sets
# class StockViewSet(viewsets.ModelViewSet):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer
#     # APIのフィルタで使えるフィールドを指定
#     filter_fields = ("id", "title", 'stock_count')


# Create your views here.
# RestAPIのview sets
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StockSerializer
    # APIのフィルタで使えるフィールドを指定
    filter_fields = ("id", "last_name", "first_name")
