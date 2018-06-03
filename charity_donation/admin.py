from django.contrib import admin
from .models import Donation, DonationLineItem

# Register your models here.

class DonationLineAdminInline(admin.TabularInline):
    model = DonationLineItem

    
class DonationModelAdmin(admin.ModelAdmin):
    inlines = (DonationLineAdminInline, )
    list_display = ["donor","date"]
    date_hierarchy = 'date'
    class Meta:
        model = Donation
        
    

admin.site.register(Donation, DonationModelAdmin)