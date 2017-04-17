from django.conf.urls import include, url
from rest_framework import routers

from backend.views import StaffViewSet
# from backend.views import StockViewSet

router = routers.DefaultRouter()
# router.register(r'stock', StockViewSet)
router.register(r'staff', StaffViewSet)

urlpatterns = [
    # qiita/api/stock/
    url(r'api/', include(router.urls, namespace='rest_framework')),
]
