from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product, Type, Cart
from .settings.base import INFO

# Create your views here.


class IndexView(View):

    def get(self, request):

        context = {'products': Product.objects.all()[:8]}
        context.update(INFO)
        return render(request, 'vegefood/index.html', context)


class ShopView(View):
    def get(self, request, prod_type=None):
        page = self.request.GET.get('page')

        if not prod_type:
            products_list = Product.objects.all()
        else:
            products_list = Product.objects.filter(type__type=prod_type)
        type_list = Type.objects.all()

        product_on_page = 4
        paginator = Paginator(products_list, product_on_page)

        try:
            products_list = paginator.page(page)
            products_list.page_tuple = tuple(paginator.page_range)
        except PageNotAnInteger:
            products_list = paginator.page(1)
        except EmptyPage:
            return redirect(reverse('shop'))

        context = {
            'page_obj': products_list,
            'type_list': type_list,
            'prod_type': prod_type
        }
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

    def get(self, request, user_id=1):
        user_id = self.request.GET.get('user_id')

        cart_list = Cart.objects.filter(user_id=user_id)
        products_list = Product.objects.all()

        context = {
            'cart_list': cart_list,
        }
        return render(request, 'vegefood/cart.html', context)


class CheckoutView(View):

    def get(self, request):
        context = INFO
        return render(request, 'vegefood/checkout.html', context)