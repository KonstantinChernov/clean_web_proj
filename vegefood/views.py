from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage

from .models import Product
from .settings.base import INFO

# Create your views here.


class IndexView(View):

    def get(self, request):

        context = {'products': Product.objects.all()[:8]}
        context.update(INFO)
        return render(request, 'vegefood/index.html', context)


class ShopView(View):
    def get(self, request, page=1):

        products_list = Product.objects.all()
        product_on_page = 4
        paginator = Paginator(products_list, product_on_page)


        # products_list = paginator.page(page)

        try:
            products_list = paginator.page(page)
            products_list.page_tuple = tuple(paginator.page_range)
        except EmptyPage:
            return redirect(reverse('shop'))

        context = {'page_obj': products_list}
        context.update(INFO)
        return render(request, 'vegefood/shop.html', context)


class AboutView(View):

    def get(self, request):
        context = INFO
        return render(request, 'vegefood/about.html', context)


class BlogView(View):

    def get(self, request):
        context = INFO
        return render(request, 'vegefood/blog.html', context)


class BlogPostView(View):

    def get(self, request):
        context = INFO
        return render(request, 'vegefood/blog-single.html', context)


class ContactView(View):

    def get(self, request):
        context = INFO
        return render(request, 'vegefood/contact.html', context)


class WishlistView(View):

    def get(self, request):
        context = INFO
        return render(request, 'vegefood/wishlist.html', context)


class ProductView(View):

    def get(self, request):
        context = INFO
        return render(request, 'vegefood/product-single.html', context)


class CartView(View):

    def get(self, request):
        context = INFO
        return render(request, 'vegefood/cart.html', context)


class CheckoutView(View):

    def get(self, request):
        context = INFO
        return render(request, 'vegefood/checkout.html', context)