from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ProjectList.as_view(), name='project_list'),
	url(r'^project/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view(), name = 'project_detail'),
]