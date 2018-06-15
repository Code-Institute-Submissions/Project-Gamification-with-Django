from django.db import models



######################### CHARITY MODEL ########################################


class Charity(models.Model):
    name = models.CharField(max_length=254, default='Charity')                  
    description = models.TextField(blank=False)                                 
    donation = models.DecimalField(max_digits=1, decimal_places=0, default=5)
    image = models.ImageField(upload_to='donations')
    
    class Meta:
        verbose_name = "Proposed Charity"
        verbose_name_plural = "Proposed Charities" 
    
    def __str__(self):
        return self.name