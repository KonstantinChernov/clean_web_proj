from rest_framework import routers

from .views import UserViewSet, ProductViewSet, CouponViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'coupons', CouponViewSet)

urlpatterns = router.urls

