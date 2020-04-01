from django.db import models
from django.db.models.signals import pre_save

# Create your models here.

class Client(models.Model):
    code       =models.AutoField
    Name       =models.CharField(max_length=999)
    Address    =models.TextField(max_length=99999)
    Tel        =models.IntegerField(max_length=10,blank=True,null=True)
    Gst_no     = models.CharField(max_length=999,blank=True,null=True)

    def __str__(self):
        return str(self.Name)


class ClientBalance(models.Model):
    Clientname =models.ForeignKey(Client,on_delete=models.CASCADE)
    Total_sales=models.DecimalField(max_digits=999999,decimal_places=2)
    Initial_payment = models.DecimalField(max_digits=999999, decimal_places=2, blank=True, null=True)
    Total_payment=models.DecimalField(max_digits=999999,decimal_places=2,blank=True,null=True)
    balance_payment=models.DecimalField(max_digits=999999,decimal_places=2,blank=True,null=True)

    def __str__(self):
        return str(self.Clientname)

def total_save(sender,instance,*args,**kwargs):
    if instance.Total_payment > instance.Initial_payment:
        instance.balance_payment =  instance.Total_payment-instance.Initial_payment
    else:
        instance.balance_payment=0.00

pre_save.connect(total_save,sender=ClientBalance)