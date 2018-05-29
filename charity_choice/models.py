from django.db import models

# Create your models here.


class Charity(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    donation = models.DecimalField(max_digits=1, decimal_places=0, default=5)
    image = models.ImageField(upload_to='donations')
    
    def __str__(self):
        return self.name