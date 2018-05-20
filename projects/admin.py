from django.contrib import admin
from .models import Project, Issue, RequiredSkills, Team, CommitSkill, ProjectState, ProjectMessage

# Register your models here.
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(RequiredSkills)
admin.site.register(Team)
admin.site.register(CommitSkill)
admin.site.register(ProjectState)
admin.site.register(ProjectMessage)