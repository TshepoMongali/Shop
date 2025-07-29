from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart
from django.http import HttpResponse

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        cart = Cart(request)
        cart.add(product)
        return redirect('cart')
    return render(request, 'shop/product_detail.html', {'product': product})

def cart_view(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart_items': list(cart)})

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect('catalog')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('view_cart')

def view_cart(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {
        'cart_items': cart.get_cart_items(),
        'total': cart.get_total()
    })


def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products})


def checkout(request):
    if request.method == 'POST':
        # Here you would normally save the order to a database and trigger payment
        Cart(request).clear()
        return HttpResponse("Order placed successfully! Thank you.")
    return render(request, 'shop/checkout.html')

