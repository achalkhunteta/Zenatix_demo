from django import forms
from models import Station

class StationForm(forms.ModelForm):
	'''
	Model Form for adding a new station
	'''

	class Meta:
		model = Station
		fields = '__all__'