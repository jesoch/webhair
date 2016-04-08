from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
from django.utils import timezone

# Create your models here.

class AdminHairDressing(models.Model):
    name = models.CharField(max_length=150)
    street = models.CharField(max_length=200)
    number = models.IntegerField(null=False)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    publish_date = models.DateField(default=date.today)


    def __unicode__(self):
        return u"%s" % self.name


class client(models.Model):

    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.TextField(default="")
    zipcode = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=9)
    schedule = models.TextField()
    description = models.TextField()
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    publish_date = models.DateField(default=date.today)


'''class Review (models.Model):
    RATING_CHOICES    =    ((1,    'one'),    (2,    'two'),    (3,    'three'),    (4,    'four'),    (5,    'five'))
    rating    =    models.PositiveSmallIntegerField('Rating(stars)',    blank=False,    default=3,
    choices=RATING_CHOICES)
    comment    =    models.TextField(blank=True,    null=True)
    user    =    models.ForeignKey(User,    default=1
    )
date    =    models.DateField(default=date.today)
class    Meta:
    abstract    =    True

class HairdressingReview(Review):
    hairdressing    =    models.ForeignKey(AdminHairDressing) '''
