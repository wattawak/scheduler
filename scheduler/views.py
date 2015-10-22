from django.shortcuts import render
from django.utils import timezone
from .models import Project
from .forms import RescheduleForm


def reschedule(days_later):					
	start_date += timedelta(days=days_later)
	design_approval += timedelta(days=days_later)
	programming_start += timedelta(days=days_later)
	programming_complete += timedelta(days=days_later)
	qa_complete += timedelta(days=days_later)
	return start_date, design_approval, programming_start, programming_complete, qa_approval


def project_list(request):
	if request.method == "POST":
		form = RescheduleForm(request.POST)
		project = Project.objects.get(#how do I get the project the form is related to???)
		if form.is_valid():
			days_later = form.cleaned_data['days_later']
			project.reschedule(days_later)
			project.save()
	else:
		form = RescheduleForm()
	projects = Project.objects.order_by('start_date')
	return render(request, 'scheduler/project_list.html', {'projects': projects, 'form': form})


