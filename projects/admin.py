from django.contrib import admin
from .models import Project, Issue, Skill, RequiredSkills, Team, CommitSkill, ProjectState

# Register your models here.
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Skill)
admin.site.register(RequiredSkills)
admin.site.register(Team)
admin.site.register(CommitSkill)
admin.site.register(ProjectState)