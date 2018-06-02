from django.db import models
from charity_choice.models import Charity

# Create your models here.
class Donation(models.Model):
    name = models.CharField(max_length=50, blank=False)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)


# class DonationLineItem(models.Model):
#     donation = models.ForeignKey(Donation, null=False, on_delete=models.CASCADE)
#     charity = models.ForeignKey(Charity, null=False, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return "{0}".format( self.charity.name)        
        
        
        


