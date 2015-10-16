from django.db import models
from django.utils import timezone


class Project(models.Model):
	project_name = models.CharField(max_length=200)
	start_date = models.DateTimeField(default=timezone.now)
	design_approval = models.DateTimeField(default=timezone.now)
	programming_complete = models.DateTimeField(default=timezone.now)
	qa_complete = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.project_name
