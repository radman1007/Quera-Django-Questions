from .models import Order
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404
from decimal import Decimal

def checkout(request, order_pk):
    try:
        order = get_object_or_404(Order, pk=order_pk)
    except Order.DoesNotExist:
        raise Http404("Order does not exist")

    total_price = sum(item.get_total_price() for item in order.items.all())
    total_price = total_price.quantize(Decimal('0.01'))
    return JsonResponse({'total_price': str(total_price)})