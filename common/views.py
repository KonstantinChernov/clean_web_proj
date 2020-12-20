from datetime import datetime
import random

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class DatetimeView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)


class RandomNumberView(View):
    def get(self, request):
        html = f"{random.randint(0, 100)}"
        return HttpResponse(html)


class IndexView(View):
    def get(self, request):
        return render(request, 'common/login.html')