from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.Categories, name='categories'),
    path('categories/<pk>', views.Products, name='products'),
    path('product/<pk>', views.Product, name='product')
]