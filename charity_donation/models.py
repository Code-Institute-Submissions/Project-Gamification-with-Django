from django.db import models
from charity_choice.models import Charity

# Create your models here.

class Donation(models.Model):
    donor = models.CharField(max_length=50, blank=False)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.donor)


class DonationLineItem(models.Model):
    donation = models.ForeignKey(Donation, null=False, on_delete=models.CASCADE)
    charity = models.ForeignKey(Charity, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=1)
    
    def __str__(self):
        return "{0}".format(self.charity.name)    