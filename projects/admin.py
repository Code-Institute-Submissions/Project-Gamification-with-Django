from django.contrib import admin
from .models import Project, Issue, Skill, RequiredSkills

# Register your models here.
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Skill)
admin.site.register(RequiredSkills)