from rest_framework import routers

from .views import UserViewSet, ProductViewSet, CouponViewSet, CartViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'carts', CartViewSet)


urlpatterns = router.urls

