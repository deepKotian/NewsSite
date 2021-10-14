from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from merch.models import Product,Category
import razorpay

def payment(request, slug):
    prod = Product.objects.filter(slug = slug).first()
    print(prod)
    context = {'prod': prod}
    return render(request , 'payment.html', context)

def merch(request):
    allMerch = Product.objects.all()
    allCat = Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        allMerch = Product.get_all_products_by_categoryid(categoryID)
    else:
        allMerch = Product.objects.all()
    context = {'allMerch': allMerch, 'allCat':allCat}
    return render(request , 'merch.html', context)
    
