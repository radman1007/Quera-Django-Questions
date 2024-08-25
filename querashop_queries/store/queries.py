from . import models



def young_employees(job: str):
    query = models.Employee.objects.filter(age__lt=30).filter(job=job)

def cheap_products():
    average_price = ;
    query = models.Product.objects.filter(price__gt=average_price)


def products_sold_by_companies():
    pass


def sum_of_income(start_date: str, end_date: str):
    pass


def good_customers():
    pass


def nonprofitable_companies():
    pass
