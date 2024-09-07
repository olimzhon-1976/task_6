
from django.db import models

class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # stock = models.IntegerField(default=0)
    # name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
class Seller(models.Model):
    objects = None
    # name = models.CharField(max_length=100)
    # email = models.EmailField()
    # phone = models.CharField(max_length=15)
    POSITION_CHOICES = [
        ('salesman', 'Продавец'),
        ('senior_salesman', 'Старший продавец'),
        ('sales_manager', 'Руководитель отдела продаж'),
    ]

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    hire_date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.position}"
class Customer(models.Model):
    objects = None
    # name = models.CharField(max_length=100)
    # email = models.EmailField()
    # phone = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Sale(models.Model):
    objects = None
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # sale_date = models.DateField()


    def __str__(self):
        return f"Sale of {self.product.name} to {self.customer.name} {self.customer.last_name}"