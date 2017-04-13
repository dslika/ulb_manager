from django.conf.urls import include, url
from rest_framework import routers

from backend.views import StockViewSet

router = routers.DefaultRouter()
router.register(r'stock', StockViewSet)

urlpatterns = [
    # qiita/api/stock/
    url(r'api/', include(router.urls)),
]
