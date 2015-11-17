from django import forms

from .models import Project

class RescheduleForm(forms.Form):
	days_later = forms.IntegerField()
	

