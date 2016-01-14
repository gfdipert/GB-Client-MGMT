from django import forms
from .models import Client
from .models import ClientBuild

class ClientForm(forms.ModelForm):

	class Meta:
		model = Client
		fields = ('name', 'apptype', 'prostatus', 'gstatus', 'appstatus', 'pstatus', 'bstatus', 'astatus', 'intro', 'appsub', 'checkapp', 'apppub', 'applaunch', 'eventdate', 'guides')

class ClientBuild(forms.ModelForm):

	class Meta:
		model = ClientBuild
		fields = ('buildusername', 'buildpassword',)