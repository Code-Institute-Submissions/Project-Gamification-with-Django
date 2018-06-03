from django.contrib import admin
from .models import MyProfile, Personality, Position


admin.site.register(Personality)
admin.site.register(Position)


class MyProfileModelAdmin(admin.ModelAdmin):
    list_display = ["owner","position", "personality"]
    class Meta:
        model = MyProfile
        
admin.site.register(MyProfile, MyProfileModelAdmin)        

