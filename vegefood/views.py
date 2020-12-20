from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DeleteView, CreateView

from .models import Product, Type, Cart, User, Wishlist
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
            'prod_type': prod_type,
            'paginator': paginator
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


class WishlistView(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'products': Wishlist.objects.filter(user_id__auth_user__username=request.user)
        }
        context.update(INFO)
        return render(request, 'vegefood/wishlist.html', context)


class WishlistViewDelete(LoginRequiredMixin, DeleteView):

    def get(self, request):
        product = request.GET.get('product')

        product_to_delete = Wishlist.objects.get(user_id__auth_user__username=request.user, product=product)
        product_to_delete.delete()
        cart_list = Wishlist.objects.filter(user_id__auth_user__username=request.user)
        context = {
            'cart_list': cart_list,
        }
        context.update(INFO)
        return redirect(request.META.get('HTTP_REFERER', '/'))


class ProductView(View):

    def get(self, request):
        product = request.GET.get('product')
        product_to_show = Product.objects.get(name=product)

        context = {'products': Product.objects.all()[:4],
                   'product_to_show': product_to_show}
        context.update(INFO)
        return render(request, 'vegefood/product-single.html', context)


class CartView(LoginRequiredMixin, View):

    def get(self, request):

        cart_list = Cart.objects.filter(user_id__auth_user__username=request.user)

        context = {
            'cart_list': cart_list,
        }
        context.update(INFO)
        return render(request, 'vegefood/cart.html', context)


class CartViewDelete(LoginRequiredMixin, DeleteView):

    def get(self, request):
        product = request.GET.get('product')

        product_to_delete = Cart.objects.get(user_id__auth_user__username=request.user, product=product)
        product_to_delete.delete()
        cart_list = Cart.objects.filter(user_id__auth_user__username=request.user)
        context = {
            'cart_list': cart_list,
        }
        context.update(INFO)
        return redirect(request.META.get('HTTP_REFERER', '/'))


class ShopAddCartView(LoginRequiredMixin, CreateView):

    def get(self, request):
        product = request.GET.get('product')
        current_product = Product.objects.get(name=product)
        if product in [i.product.name for i in Cart.objects.filter(user_id__auth_user__username=request.user)]:
            current_product = Cart.objects.get(user_id__auth_user__username=request.user, product=current_product)
            current_product.count += 1
            current_product.save()
        else:
            current_user = User.objects.get(auth_user=request.user)
            Cart.objects.create(user_id=current_user, product=current_product, count=1)
        return redirect(request.META.get('HTTP_REFERER', '/'))


class ShopAddWishlistView(LoginRequiredMixin, CreateView):

    def get(self, request):
        product = request.GET.get('product')
        current_product = Product.objects.get(name=product)
        if product in [i.product.name for i in Wishlist.objects.filter(user_id__auth_user__username=request.user)]:
            current_product = Wishlist.objects.get(user_id__auth_user__username=request.user, product=current_product)
            current_product.count += 1
            current_product.save()
        else:
            current_user = User.objects.get(auth_user=request.user)
            Wishlist.objects.create(user_id=current_user, product=current_product, count=1)
        return redirect(request.META.get('HTTP_REFERER', '/'))


class CheckoutView(View):

    def get(self, request):
        context = INFO
        return render(request, 'vegefood/checkout.html', context)

