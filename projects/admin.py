from django.contrib import admin
from .models import *
from django.db.models.functions import Trunc
from datetime import datetime
from django.db.models import Count, DateField
from django.db.models import Min, Max

# Register your models here.


admin.site.register(Team)
admin.site.register(CommitSkill)
admin.site.register(ProjectState)
admin.site.register(ProjectMessage)



class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ["name","status", 'proposed_by', 'budget']
    class Meta:
        model = Project
    
admin.site.register(Project, ProjectModelAdmin)


class IssueModelAdmin(admin.ModelAdmin):
    list_display = ["name","project","cost","assigned_to"]
    class Meta:
        model = Issue

admin.site.register(Issue, IssueModelAdmin)


class RequiredSkillsModelAdmin(admin.ModelAdmin):
    list_display = ["project","html","css","js","db","python"]
    class Meta:
        model = RequiredSkills

admin.site.register(RequiredSkills, RequiredSkillsModelAdmin)





# @admin.register(ProjectMessageSummary)
# class ProjectMessageSummary(admin.ModelAdmin):
#     change_list_template = 'admin/project_message_summary_change_list.html'
#     date_hierarchy = 'message_date'
    
#     list_filter = (
#         'project',
#         )
    