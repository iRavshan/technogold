from django.shortcuts import render,HttpResponse
from . import models

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
        context = {
            'product': product
        }
        return render(request, 'store/product.html', context)
    return HttpResponse('Hech narsa topilmadi')