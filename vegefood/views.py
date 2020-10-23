from django.shortcuts import render
from django.views import View
from .settings.base import INFO
# Create your views here.


class IndexView(View):

    def get(self, request):
        context = INFO # dict
        return render(request, 'vegefood/index.html', context)



class ShopView(View):

    def get(self, request):
        d = {'page_obj': [
            {
                'image': ...,
                'name':...,
                'discount': ...,
                'price_full': ...,
                'price_sale': ...,
            }
        ]}
        context = INFO # dict
        return render(request, 'vegefood/shop.html', context)