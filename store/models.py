from django.db import models

class Products(models.Model):
    # sku = models.CharField(max_length=10, primary_key=True)
    MEMBERSSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSSHIP_BRONZE)
    collection =models.ForeignKey('Collections', on_delete=models.PROTECT) # ForeignKey to Collections model

class Customers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.DecimalField(max_digits=15, decimal_places=0)
    birth_date = models.DateField(null=True)
    #IMP Here all these model we dont have Id field because django automatically create Id field for each model

class Orders(models.Model):
    PENDING_STATUS ='P'
    COMPLETE_STATUS ='C'
    FAILED_STATUS = 'F'
    STATUS_CHOICES=[
        (PENDING_STATUS,"Pending"),
        (COMPLETE_STATUS,"Complete"),
        (FAILED_STATUS,"Failed"),
    ]
    placed_at=models.DateTimeField(auto_now_add=True) #when first order is created django automatically populate this field with current date
    payment_status=models.CharField(max_length=1,choices=STATUS_CHOICES,default=PENDING_STATUS)
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE) #ForeignKey to Customers model

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE) # One-to-Many relationship with Customers
    #Why not one-to-many has primary key? becz primary key limit one record only but one customer can have multiple addresses
    #customer = models.OneToOneField(Customers, on_delete=models.CASCADE ,primary_key=True) # One-to-One relationship with Customers

class Collections(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name='+')
    #related_name='+' means we dont need reverse relationship from Products to Collections
class Carts(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
class Items(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE) # ForeignKey to Orders model
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE) # ForeignKey to Carts model
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
