from django.db import models

# Create your models here.
class Product(models.Model):
    class Meta:
        app_label = 'myapp'
    product_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_code

    
class Import(models.Model):
    class Meta:
        app_label = 'myapp'
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE)
    import_date = models.DateField()
    number = models.IntegerField(default=0)
    supplier = models.CharField(max_length=200)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.product_code)
        
class Export (models.Model):
    class Meta:
        app_label = 'myapp'
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE)
    export_date = models.DateField()
    number = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=200)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.product_code)

class Inventory (models.Model):
    class Meta:
        app_label = 'myapp'
    product_code = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    new = models.IntegerField(default=0)
    old = models.IntegerField(default=0)
    unit = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.product_code)
