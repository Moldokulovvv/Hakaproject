from django.shortcuts import render, redirect
from django.urls import reverse

import braintree

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order




def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         ticket=item['ticket'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()

            # Сохранение заказа в сессии.
            request.session['order_id'] = order.id
            # Перенаправление на страницу оплаты.
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm
    return render(request, 'order/create.html',
                  {'cart': cart, 'form': form})




