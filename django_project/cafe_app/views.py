from django.shortcuts import render, redirect
from .models import Product, Order

# Create your views here.

# View for Home Page
def home(request):
    return render(request, 'cafe_app/home.html')

# View for About Page
def about(request):
    return render(request, 'cafe_app/about.html')

# View for Contact Page
def contact(request):
    return render(request, 'cafe_app/contact.html')

# View for Menu Page
def menu(request):
    products = Product.objects.all()
    return render(request, 'cafe_app/menu.html', {'products': products})

# View for Order Page
def order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        product = Product.objects.get(id=product_id)
        Order.objects.create(product=product, quantity=quantity, customer_name=customer_name, customer_phone=customer_phone)
        return redirect('home')
    else:
        products = Product.objects.all()
        return render(request, 'cafe_app/order.html', {'products': products})
