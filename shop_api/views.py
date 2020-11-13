from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework import mixins, status

from vegefood.models import User, Product, Coupon, Cart
from .serializers import UserSerializer, ProductSerializer, CouponSerializer, CartSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        filter_params = {param: request.GET[param] for param in request.GET}

        queryset = self.get_queryset()
        filter_queryset = queryset.filter(**filter_params)

        serializer = self.get_serializer(filter_queryset, many=True)

        return Response(serializer.data)


class CouponViewSet(mixins.RetrieveModelMixin,
                    GenericViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    lookup_field = 'name'


class CartViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(methods=['GET'], detail=False)
    def add(self, request):
        product = request.GET['product']
        user_id = request.GET['user_id']
        count = request.GET['count']

        serializer = self.get_serializer(data=dict(user_id=user_id, product=product, count=count))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

    def list(self, request, *args, **kwargs):
        filter_params = {param: request.GET[param] for param in request.GET}

        queryset = self.get_queryset()
        filter_queryset = queryset.filter(**filter_params)

        serializer = self.get_serializer(filter_queryset, many=True)

        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def delete(self, request):
        product = request.GET['product']
        user_id = request.GET['user_id']

        self.get_queryset().get(user_id__id=user_id, product__id=product).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


