from django.db import models



class Product(models.Model):
    name=models.CharField(max_length=35)
    image=models.ImageField(upload_to='products/',blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    details=models.TextField()

    def __str__(self):
        return self.name 
    

