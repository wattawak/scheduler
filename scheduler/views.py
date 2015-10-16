from django.shortcuts import render
from .models import Project

def project_list(request):
	projects = Project.objects.all()
	return render(request, 'scheduler/project_list.html', {'projects': projects})
