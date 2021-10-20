from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from merch.models import Product,Category,Payment
from django.http import HttpResponse
from news_site.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay

def payment(request, slug):
    if request.method == 'POST':
        payment =Payment()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment.name = name
        payment.phone = phone
        payment.address = address
        payment.save() 
       

        client = razorpay.Client(auth=("rzp_test_yOgTa9YwwHLKDR", "qDmtqkDq7Rs3OIpFDd7JDtRR"))
        DATA = {
        "amount": 10000,
        "currency": "INR",
        "receipt": "receipt#1",
        }
        payment_order = client.order.create(data=DATA)
        payment_order_id = payment_order['id']
        prod = Product.objects.filter(slug = slug).first()
        print(prod)
        context = {
            'prod': prod,
            'api_key': RAZORPAY_API_KEY,
            'order_id': payment_order_id,
            }
  
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
    
