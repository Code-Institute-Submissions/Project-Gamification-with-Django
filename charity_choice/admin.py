from django.contrib import admin
from .models import Charity


## Displaying Charity in Admin Panel

class CharityModelAdmin(admin.ModelAdmin):
    list_display = ["name","description"]
    class Meta:
        model = Charity

admin.site.register(Charity, CharityModelAdmin)





