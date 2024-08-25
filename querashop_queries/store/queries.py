from . import models

def young_employees(job: str):
    query = models.Employee.objects.filter(age__lt=30).filter(job=job)

def cheap_products():
    products = models.Product.objects.all()
    average_price = sum(item.price for item in products) // len(products)
    query = models.Product.objects.filter(price__gt=average_price)


def products_sold_by_companies():
    models.Company.objects.all()


def sum_of_income(start_date: str, end_date: str):
    query = models.Order.objects.filter(time__range=[start_date, end_date])


def good_customers():
    pass


def nonprofitable_companies():
    pass