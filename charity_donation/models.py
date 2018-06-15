from django.db import models
from charity_choice.models import Charity



######################### DONOR REGISTRY MODEL #################################

class Donation(models.Model):
    donor = models.CharField(max_length=50, blank=False, default="Donor")
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.donor)
    
    class Meta:
        verbose_name = "User Donation"
        verbose_name_plural = "User Donations"     


######################### DONATION MODEL #######################################


class DonationLineItem(models.Model):
    donation = models.ForeignKey(Donation, null=False, on_delete=models.CASCADE)
    charity = models.ForeignKey(Charity, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=1)
    

    def __str__(self):
        return str(self.charity.name)    