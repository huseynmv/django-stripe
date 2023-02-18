from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return f'{self.price / 100}'
