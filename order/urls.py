from rest_framework import routers

from order.views import OrderViewSet

router = routers.DefaultRouter()
router.register('', viewset=OrderViewSet)

order_urls = router.urls
