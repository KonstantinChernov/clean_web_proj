from django.urls import path
from .views import BlogView, BlogPostView

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/post/', BlogPostView.as_view(), name='blogpost'),
]
