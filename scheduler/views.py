from django.shortcuts import render
from django.utils import timezone
from .models import Project
from .forms import RescheduleForm


def project_list(request):
	if request.method == "POST":
		form = RescheduleForm(request.POST)
		#how do I get the project the form is related to???
		# project = Project.objects.get()
		if form.is_valid():
			days_later = form.cleaned_data['days_later']
			project_id = form.cleaned_data['project_id']
			project = Project.objects.get(pk=project_id)
			project.reschedule(days_later)
			project.save()
	else:
		form = RescheduleForm()
	projects = Project.objects.order_by('start_date')
	return render(request, 'scheduler/project_list.html', {'projects': projects, 'form': form})


