from django.shortcuts import render,HttpResponse
from . import models
import random

def Categories(request):
    context={
        'categories': models.Category.objects.all()
    }
    return render(request, 'store/categories.html', context)

def Products(request, pk):
    get_category = models.Category.objects.get(id=pk)
    if get_category is not None:
        context={
            'products': models.Product.objects.filter(category=get_category),
            'cat_name': get_category.name
        }
        return render(request, 'store/products.html', context)
    return HttpResponse('Hech narsa topilmadi')

def Product(request, pk):
    product=models.Product.objects.get(id=pk)
    if product is not None:
        products = list(models.Product.objects.filter(category=product.category))
        product_images = models.ProductImage.objects.filter(product=product)
        reccom_products = random.sample(products, 1)
        #while product in reccom_products:
            #reccom_products.remove(product)
            #reccom_products.append(random.choice(products))
        context = {
            'product': product,
            'reccom_products': reccom_products,
            'product_images': product_images
        }
        return render(request, 'store/product.html', context)
    return HttpResponse('Hech narsa topilmadi')