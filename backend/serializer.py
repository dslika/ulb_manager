from rest_framework import serializers

from backend.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ("id", "title", 'stock_count')
