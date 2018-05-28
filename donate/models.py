from django.db import models
from projects.models import Project

# Create your models here.
class Donation(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    position = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class SupportedProject(models.Model):
    donation = models.ForeignKey(Donation, null=False, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.project.name, self.project.budget)