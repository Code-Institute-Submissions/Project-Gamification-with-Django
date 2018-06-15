from django.contrib import admin
from .models import Donation, DonationLineItem


## Displaying Single Donation in Admin Panel

class DonationLineAdminInline(admin.TabularInline):
    model = DonationLineItem


## Donor & Date display in Admin Panel
    
class DonationModelAdmin(admin.ModelAdmin):
    inlines = (DonationLineAdminInline, )
    list_display = ["donor","date"]
    date_hierarchy = 'date'
    class Meta:
        model = Donation
        
    

admin.site.register(Donation, DonationModelAdmin)