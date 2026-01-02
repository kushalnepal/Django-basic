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