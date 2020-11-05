from django.urls import path, include
from .views import IndexView, ShopView, AboutView

urlpatterns = [
    path('', IndexView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
    path('about/', AboutView.as_view(), name='about'),
]

