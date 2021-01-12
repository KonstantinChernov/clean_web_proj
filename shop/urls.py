from django.urls import path
from .views import IndexView, ShopView, AboutView,\
    ContactView, WishlistView, ProductView, CartView, CheckoutView, CartViewDelete, \
    ShopAddCartView, WishlistViewDelete, ShopAddWishlistView

urlpatterns = [
    path('', IndexView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<str:prod_type>/', ShopView.as_view(), name='shop'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('product/', ProductView.as_view(), name='product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('delete_from_cart/', CartViewDelete.as_view(), name='delete_from_cart'),
    path('delete_from_wishlist/', WishlistViewDelete.as_view(), name='delete_from_wishlist'),
    path('add_to_cart/', ShopAddCartView.as_view(), name='add_to_cart'),
    path('add_to_wishlist/', ShopAddWishlistView.as_view(), name='add_to_wishlist'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
