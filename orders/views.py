from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from item.models import Item

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order, created = Order.objects.get_or_create(user=request.user, is_completed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, item=item, defaults={'price': item.price})

    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('orders:cart_detail')

@login_required
def cart_detail(request):
    order = get_object_or_404(Order, user=request.user, is_completed=False)
    return render(request, 'orders/cart_detail.html', {'order': order})

@login_required
def purchase(request):
    order = get_object_or_404(Order, user=request.user, is_completed=False)
    order.is_completed = True
    order.save()
    return render(request, 'orders/purchase_success.html', {'order': order})
