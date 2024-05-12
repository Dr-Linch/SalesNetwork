from django.db import models
from users.models import NULLABLE
from datetime import datetime, timedelta


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='')
    model = models.CharField(max_length=100, verbose_name='')
    launch_date = models.DateTimeField(default=datetime.now()+timedelta(weeks=2), verbose_name='')


class Provider(models.Model):

    LEVELS = (
        ('1', 'Завод'),
        ('2', 'Розничная сеть'),
        ('3', 'Индивидуальный предприниматель')
    )

    level = models.CharField(default=1, max_length=1, choices=LEVELS)
    name = models.CharField(max_length=100, verbose_name='Provide Name')
    email = models.EmailField(verbose_name='Provide Email')
    country = models.CharField(max_length=100, verbose_name='Provider Country')
    citi = models.CharField(max_length=100, verbose_name='Provider Citi')
    street = models.CharField(max_length=100, verbose_name='Provider Street')
    house_number = models.IntegerField(verbose_name='Provider House Number')
    products = models.ManyToManyField(Product, **NULLABLE)
    self_provider = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE)
    provider_debt = models.BigIntegerField(verbose_name='Задолженность', default=0)
    created_at = models.DateTimeField(default=datetime.now(), verbose_name='Creation time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'
