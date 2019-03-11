from django import forms
from .models import Pages

class UploadDataForm(forms.ModelForm):
	class Meta:
		model = Pages
		fields = ['data']