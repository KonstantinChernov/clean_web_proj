from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class HelloView(View):
    def get(self, request):
        html = f"<html><body><h1>Hello World</h1></body></html>"
        return HttpResponse(html)
