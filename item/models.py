from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.name} {self.description} {self.price}'
