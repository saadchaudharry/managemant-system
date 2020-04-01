from django.db import models

# Create your models here.

class Products(models.Model):
    Img     =models.ImageField()
    Title   =models.CharField(max_length=1200)
    Price   =models.DecimalField(max_digits=9999999,decimal_places=2)

    def __str__(self):
        return str(self.Title)



class Prod_quantity(models.Model):
    Prod    =models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self):
        return str(self.Prod)