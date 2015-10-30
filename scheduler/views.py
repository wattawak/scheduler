from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, FormView, View
from django.core.urlresolvers import reverse
from django.views.generic.detail import SingleObjectMixin


from .models import Project
from .forms import RescheduleForm

class ProjectList(ListView):
	model = Project
	template_name = 'scheduler/project_list.html'
	context_object_name = 'project_list'
	def get_queryset(self):
		return Project.objects.order_by('start_date')
		
		
class ProjectDetailView(DetailView):
	model = Project
	context_object_name = 'project_detail'
	
	def get_context_data(self, **kwargs):
		context = super(ProjectDetailView, self).get_context_data(**kwargs)
		context['form'] = RescheduleForm()
		return context		
	
class ProjectDetailFormView(SingleObjectMixin, FormView):
	template_name = 'scheduler/project_detail.html'
	form_class = RescheduleForm
	model = Project
	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		self.object.reschedule(days_later)
		self.object.save()
	
	def get_success_url(self):
		return reverse('project_detail', kwargs={'pk': self.object.pk})
		
	
class ProjectDetail(View):

	def get(self, request, *args, **kwargs):
		view = ProjectDetailView.as_view()
		return view(request, *args, **kwargs)
		
	def post(self, request, *args, **kwargs):
		view = ProjectDetailFormView.as_view()
		return view(request, *args, **kwargs)


