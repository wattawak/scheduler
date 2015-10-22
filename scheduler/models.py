from django.db import models
from django.utils import timezone
from datetime import timedelta


class Project(models.Model):
	project_name = models.CharField(max_length=200)
	start_date = models.DateField(default=timezone.now)
	design_approval = models.DateField(default=timezone.now)
	programming_start = models.DateField(default=timezone.now)
	programming_complete = models.DateField(default=timezone.now)
	qa_complete = models.DateField(default=timezone.now)	
	
	def __str__(self):
		return self.project_name
