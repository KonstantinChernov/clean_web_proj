from django.urls import path, include
from .views import IndexView, ShopView

urlpatterns = [
    path('', IndexView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
]

