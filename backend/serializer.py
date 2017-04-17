from rest_framework import serializers

# from backend.models import Stock
from backend.models import Staff


# class StockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stock
#         fields = ("id", "title", 'stock_count')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ("id", "last_name", "first_name")
