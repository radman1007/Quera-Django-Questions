from . import models
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from django.db.models import Sum


def young_employees(job: str):
    query = models.Employee.objects.filter(age__lt=30).filter(job=job)

def cheap_products():
    products = models.Product.objects.all()
    average_price = sum(item.price for item in products) // len(products)
    query = models.Product.objects.filter(price__gt=average_price)


def products_sold_by_companies():
    pass


def sum_of_income(start_date: str, end_date: str):
    query = models.Order.objects.filter(time__range=[start_date, end_date]).aggregate(total=Sum('price'))
    print(query)
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
    pass