from django.contrib import admin
from .models import *
from django.db.models.functions import Trunc
from datetime import datetime
from django.db.models import Count, DateField
from django.db.models import Min, Max





admin.site.register(ProjectState)

## Displaying Projects in Admin Panel


class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ["name","status", 'proposed_by', 'budget']
    class Meta:
        model = Project
    
admin.site.register(Project, ProjectModelAdmin)


## Displaying Issues in Admin Panel


class IssueModelAdmin(admin.ModelAdmin):
    list_display = ["name","project","cost","assigned_to"]
    
    list_filter = (
    "project",
    )    
    class Meta:
        model = Issue

admin.site.register(Issue, IssueModelAdmin)


## Displaying Skillset List in Admin Panel


class RequiredSkillsModelAdmin(admin.ModelAdmin):
    list_display = ["project","html","css","js","db","python"]
    class Meta:
        model = RequiredSkills

admin.site.register(RequiredSkills, RequiredSkillsModelAdmin)


## Displaying Team Membership in Admin Panel


class TeamMemberModelAdmin(admin.ModelAdmin):
    list_display = ["current_user","user_projects"]
    
    search_fields = ["current_user","user_projects"]
    class Meta:
        model = TeamMember
        
    def user_projects(self, obj):
        return "\n".join([p.name for p in obj.projects.all()])    

admin.site.register(TeamMember, TeamMemberModelAdmin)


## Displaying Team Membership in Admin Panel


class CommitSkillModelAdmin(admin.ModelAdmin):
    list_display = ["project","user","skill"]
    search_fields = ["user","skill"]
    list_filter = (
    "project","skill"
    ) 
    
    class Meta:
        model = CommitSkill

admin.site.register(CommitSkill, CommitSkillModelAdmin)


## Displaying Project Messages in Admin Panel

class ProjectMessageModelAdmin(admin.ModelAdmin):
    list_display = ["project","message_date", "message"]
    # change_list_template = 'admin/project_message_summary_change_list.html'
    date_hierarchy = 'message_date'
    search_fields = ["message"]
    list_filter = (
        'project',
        )
    
admin.site.register(ProjectMessage, ProjectMessageModelAdmin)    



## Displaying Gamification Advices in Admin Panel

class GamificationAdviceModelAdmin(admin.ModelAdmin):
    list_display = ["name","advice"]
    
    class Meta:
        model = GamificationAdvice

admin.site.register(GamificationAdvice, GamificationAdviceModelAdmin)