from django.shortcuts import render
from django.utils import timezone
from .models import Project

def project_list(request):
	projects = Project.objects.order_by('start_date')
	return render(request, 'scheduler/project_list.html', {'projects': projects})
