from django.contrib import admin
from .models import *
from django.db.models.functions import Trunc
from datetime import datetime
from django.db.models import Count, DateField
from django.db.models import Min, Max

# Register your models here.
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(RequiredSkills)
admin.site.register(Team)
admin.site.register(CommitSkill)
admin.site.register(ProjectState)
admin.site.register(ProjectMessage)


@admin.register(ProjectMessageSummary)
class ProjectMessageSummary(admin.ModelAdmin):
    change_list_template = 'admin/project_message_summary_change_list.html'
    date_hierarchy = 'message_date'
    
    list_filter = (
        'project',
        )
    
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        
        try:
                qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
                return response 
                
        metrics = {
            'total': Count('id'),
            'total_project': Count('project'),
        }        
        
        response.context_data['summary'] = list(
            qs
            .values('project')
            .annotate(**metrics)
            .order_by('-total_project')
        )
        
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        
        summary_over_time = qs.annotate(
            period=Trunc(
                'message_date',
                'day',
                output_field=DateField(),
            ),
        ).values('period').annotate(total=Count('project')).order_by('period')

        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)

        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': \
               ((x['total'] or 0) - low) / (high - low) * 100 
               if high > low else 0,
        } for x in summary_over_time]
        
        
        return response