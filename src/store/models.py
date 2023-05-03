from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, null=False)
    desc = models.TextField()
    cover_img = models.FileField(upload_to='categories/', null=True, default=None)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=350, null=False)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, default=None, null=True)
    cover_img = models.FileField(upload_to='products/', null=True, default=None)
    price = models.PositiveIntegerField(default=0, null=True)
    desc = models.TextField(null=True)
    def __str__(self) -> str:
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, default=None, null=False)
    image = models.FileField(upload_to='products/', null=False, default=None)
    
