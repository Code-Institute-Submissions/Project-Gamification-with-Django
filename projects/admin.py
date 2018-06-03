from django.contrib import admin
from .models import *
from django.db.models.functions import Trunc
from datetime import datetime
from django.db.models import Count, DateField
from django.db.models import Min, Max

# Register your models here.


admin.site.register(ProjectState)


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ["name","status", 'proposed_by', 'budget']
    class Meta:
        model = Project
    
admin.site.register(Project, ProjectModelAdmin)


class IssueModelAdmin(admin.ModelAdmin):
    list_display = ["name","project","cost","assigned_to"]
    
    list_filter = (
    "project",
    )    
    class Meta:
        model = Issue

admin.site.register(Issue, IssueModelAdmin)


class RequiredSkillsModelAdmin(admin.ModelAdmin):
    list_display = ["project","html","css","js","db","python"]
    class Meta:
        model = RequiredSkills

admin.site.register(RequiredSkills, RequiredSkillsModelAdmin)


class TeamModelAdmin(admin.ModelAdmin):
    list_display = ["current_user","user_projects"]
    class Meta:
        model = Team
        
    def user_projects(self, obj):
        return "\n".join([p.name for p in obj.projects.all()])    

admin.site.register(Team, TeamModelAdmin)



class ProjectMessageModelAdmin(admin.ModelAdmin):
    list_display = ["project","message_date", "message"]
    # change_list_template = 'admin/project_message_summary_change_list.html'
    date_hierarchy = 'message_date'
    search_fields = ["message"]
    list_filter = (
        'project',
        )
    
admin.site.register(ProjectMessage, ProjectMessageModelAdmin)    