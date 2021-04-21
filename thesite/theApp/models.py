from django.db import models

# Create your models here.


class Product(models.Model):
    P_id = models.CharField(max_length=100)
    P_name = models.CharField(max_length=100)
    qty = models.IntegerField()
    


class Location(models.Model):
    Loc_id = models.CharField(max_length=100)
    Loc_name = models.CharField(max_length=100)
    
class Inventory(models.Model):
    Prod = models.CharField(max_length=100)
    Prod_id = models.CharField(max_length=100)
    Loc_name = models.CharField(max_length=100, null=True, default=None, blank=True)
    Quantity = models.IntegerField()

    
class ProductMovement(models.Model):
    Movement_id = models.CharField(max_length=100)
    Prod_id = models.CharField(max_length=100)
    Loc_From = models.CharField(max_length=100, null=True, default=None, blank=True)
    Loc_To = models.CharField(max_length=100)
    timestamp= models.DateField(null=True, blank=True)
    Quantity = models.IntegerField()

    def __str__(self):
        return self.title
