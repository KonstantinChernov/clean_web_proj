from django.shortcuts import render
from django.views import View

from .models import News
from .settings.base import INFO


class BlogView(View):

    def get(self, request):
        context = {
            'news': News.objects.all()
        }
        context.update(INFO)
        return render(request, 'blog/blog.html', context)


class BlogPostView(View):

    def get(self, request):
        context = INFO
        return render(request, 'blog/blog-single.html', context)
