import json

from django.http import HttpResponse, HttpResponseNotFound

from .models import Order, OrderItem


def get_first_or_none(qs):
    if not qs.exists():
        return None
    return qs.first()


def checkout(request, order_pk):
    order = get_first_or_none(Order.objects.filter(pk=order_pk))
    if order is None:
        return HttpResponseNotFound()
    order_items = list(OrderItem.objects.filter(order=order))
    cost = 0
    for order_item in order_items:
        cost += order_item.product.price * order_item.quantity
    result = {'total_price': "{:.2f}".format(cost)}
    return HttpResponse(json.dumps(result), content_type='application/json')
