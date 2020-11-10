from django.urls import path, include
from .views import IndexView, ShopView, AboutView, BlogView, \
    BlogPostView, ContactView, WishlistView, ProductView, CartView, CheckoutView, ShopTypeView

urlpatterns = [
    path('', IndexView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<str:prod_type>/', ShopTypeView.as_view(), name='shoptype'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/post/', BlogPostView.as_view(), name='blogpost'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('product/', ProductView.as_view(), name='product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

]
