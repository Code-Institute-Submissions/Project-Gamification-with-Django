from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(RequiredSkills)
admin.site.register(Team)
admin.site.register(CommitSkill)
admin.site.register(ProjectState)
admin.site.register(ProjectMessage)


@admin.register(ProjectSummary)
class ProjectSummaryAdmin(admin.ModelAdmin):
    project_summary_template = 'admin/project_summary_change_list.html'
    status_hierarchy = 'status'