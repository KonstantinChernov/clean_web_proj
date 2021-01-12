from django.db import models
from shop.models import User
# Create your models here.


class News(models.Model):

    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    photo = models.ImageField()
    author = models.ForeignKey('shop.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


