from django import forms
from .models import Computer
os_choices =[('window','Windows'),('linux','Linux')]
class addcomputerForm(forms.ModelForm):

	class Meta:
		model = Computer
		exclude = []
		
		fields = ['ip_address','SerialKey','HostName','BrandName','OsName','OsVersion','Processor','Ram','ExternalStorage','Location']
	# ip_address = forms.CharField(required=True,widget=forms.TextInput)
	# SerialKey = forms.CharField(required = True,max_length= 100)
	# HostName = forms.CharField(required = True,max_length= 100,help_text = 'Example:PNQ...')
	# BrandName = forms.CharField(required = True,max_length= 100)
	# OsName = forms.CharField(widget=forms.Select(choices =os_choices ))
	# OsVersion = forms.IntegerField()
	# Processor = forms.CharField(required = True,max_length= 100)
	# Ram = forms.CharField(required = True,max_length= 100)
	# ExternalStorage = forms.CharField(required = True,max_length= 100)
	# Location = forms.CharField(required = True,max_length= 100)