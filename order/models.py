from django.db import models
from django.db.models.signals import pre_save
from client.models import Client
from product.models import Prod_quantity


# Create your models here.

STATUS_CHOICES = [
    ('inital', 'inital'),
    ('process', 'process'),
    ('deliver', 'deliver'),
    ('cancel', 'cancel'),
]
class orders(models.Model):
    date =models.DateTimeField(auto_now=True)
    client =models.ForeignKey(Client,on_delete=models.CASCADE,blank=True,null=True)
    products = models.ManyToManyField(Prod_quantity,blank=True)
    status =models.CharField(max_length=122251985,choices=STATUS_CHOICES, default='inital')
    Initial_payment = models.DecimalField(max_digits=999999, decimal_places=2, blank=True, null=True)
    Total_payment = models.DecimalField(max_digits=999999, decimal_places=2, blank=True, null=True)
    balance_payment = models.DecimalField(max_digits=999999, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.client)

def total_save(sender,instance,*args,**kwargs):
    if instance.Total_payment > instance.Initial_payment:
        instance.balance_payment =  instance.Total_payment-instance.Initial_payment
    else:
        instance.balance_payment=0.00

pre_save.connect(total_save,sender=orders)