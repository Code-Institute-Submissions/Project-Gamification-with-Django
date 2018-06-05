from django.contrib import admin
from .models import *


admin.site.register(Personality)
admin.site.register(Position)
admin.site.register(PersonalityQuestion)


class MyProfileModelAdmin(admin.ModelAdmin):
    list_display = ["owner","position", "personality"]
    class Meta:
        model = MyProfile
        
    list_filter = (
        "position", "personality"
        )    
        
admin.site.register(MyProfile, MyProfileModelAdmin)        

