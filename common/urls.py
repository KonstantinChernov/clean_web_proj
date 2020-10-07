from django.urls import path
from .views import DatetimeView
from .views import RandomNumberView
from .views import IndexView

urlpatterns = [
    path('datetime/', DatetimeView.as_view()),
    path('random/', RandomNumberView.as_view()),
    path('', IndexView.as_view()),
]