from django.contrib import admin
from .models import Donation, DonationLineItem
# Register your models here.


class DonationLineAdminInline(admin.TabularInline):
    model = DonationLineItem
    
class DonationAdmin(admin.ModelAdmin):
    inlines = (DonationLineAdminInline, )
    
    
admin.site.register( Donation, DonationAdmin)    