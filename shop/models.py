from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User as UserAuth
# Create your models here.


class User(models.Model):
    SEX = (
        ('1', 'Мужчина'),
        ('0', 'Женщина')
    )
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    phone_number = models.CharField(max_length=12, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX, null=True, blank=True)

    city = models.CharField(max_length=20, editable=False)
    age = models.IntegerField(default=18)

    auth_user = models.OneToOneField(UserAuth, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(max_length=20, unique=True)
    image = models.ImageField()
    price = models.FloatField()
    discount = models.IntegerField(blank=True, null=True)
    price_sale = models.FloatField()
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    type = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.type}'


class Cart(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    count = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.count * self.product.price_sale

    def __str__(self):
        return f"{self.user_id} - {self.product}"

    class Meta:
        unique_together = (('user_id', 'product'), )


class Wishlist(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    count = models.IntegerField()
    # create_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.count * self.product.price_sale

    def __str__(self):
        return f"{self.user_id} - {self.product}"

    class Meta:
        unique_together = (('user_id', 'product'), )


class Coupon(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    value = models.IntegerField()
    min_coast = models.IntegerField()
    start_at = models.DateTimeField()
    finish_at = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"

    def check_date(self):
        if self.start_at > self.finish_at:
            raise ValidationError({'finish_at': ["Start date must be less finish date"]})
