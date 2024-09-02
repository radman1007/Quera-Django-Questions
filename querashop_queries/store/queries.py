from . import models
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from django.db.models import Sum, Avg


def young_employees(job: str):
    query = models.Employee.objects.filter(age__lt=30).filter(job=job)
    return query

def cheap_products():
    products = models.Product.objects.all()
    average_price = sum(item.price for item in products) // len(products)
    query = models.Product.objects.filter(price__gt=average_price).order_by('price')
    return query


def products_sold_by_companies():
    query = models.Company.objects.annotate(total_sold=Sum('product_set__sold')).values_list('name', 'total_sold')
    return query


def sum_of_income(start_date: str, end_date: str):
    query = models.Order.objects.filter(time__range=[start_date, end_date]).aggregate(total=Sum('price'))
    return query['total'] or 0


def good_customers():
    one_month_ago = timezone.now() - timedelta(days=30)
    query = models.Customer.objects.filter(level="G"
                                ).filter(order__time__gte=one_month_ago
                            ).annotate(order_count=Count('orders')
                        ).filter(order_count__gt=10
                    ).values('name', 'phone')
                        
    for customer in query:
        print((customer['name'], customer['phone']))

def nonprofitable_companies():
    query = models.Company.objects.annotate(
        low_selling_product_count=models.Count(
            'product', filter=models.Q(product__sold__lt=100))
        ).filter(low_selling_product_count__gte=4
                 ).values_list('name', flat=True)
    return query