from rest_framework import routers

from user.views import UserViewSet

router = routers.DefaultRouter()
router.register('', viewset=UserViewSet)

user_urls = router.urls
