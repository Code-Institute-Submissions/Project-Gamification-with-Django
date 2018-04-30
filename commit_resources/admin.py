from django.contrib import admin
from .models import Donation, SupportedProject
# Register your models here.


class SupportedProjectAdminInline(admin.TabularInline):
    model = SupportedProject
    
class DonationAdmin(admin.ModelAdmin):
    inlines = (SupportedProjectAdminInline, )
    
    
admin.site.register( Donation, DonationAdmin)    