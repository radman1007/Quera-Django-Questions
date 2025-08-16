from cabin.models import *
from django.db.models import Sum, F, Value, Q, Count
from django.db.models.functions import Coalesce
from math import sqrt

# def query_0(x):
#     q = Driver.objects.filter(rating__gt=x)
#     return q


def query_1(x):
    q = Payment.objects.filter(ride__car__owner_id=x).aggregate(total_amount=Sum('amount'))['total_amount']
    return q


def query_2(x):
    q = Ride.objects.filter(request__rider__account=x).select_related('rider__account')
    return q


def query_3(t):
    q = Ride.objects.annotate(duration=F('dropoff_time')-F('pickup_time')).filter(duration__gt=t).count()
    return q


def query_4(x, y, r):
    q = Driver.objects.annotate(distance=sqrt((F('x')-Value(x))**2+(F('y')-Value(y))**2)).filter(distance__lte=r, active=True)
    return q


def query_5(n, c):
    q = Driver.objects.annotate(ride_count=Coalesce(Count('car__ride'),0)).filter(ride_count__gte=n).filter(Q(car__car_type="A")|Q(car__color=c)).distinct()
    return q


def query_6(x, t):
    q = Ride.objects.annotate(ride_count=Count('ride'), total=Sum('ride__payment__amount')).filter(ride_count__gte=x, total__gt=t)
    return q


def query_7():
    q = Driver.objects.filter()
    return q


def query_8():
    q = 'your query here'
    return q


def query_9(n, t):
    q = 'your query here'
    return q


def query_10():
    q = 'your query here'
    return q
