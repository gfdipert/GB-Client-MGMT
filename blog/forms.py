from django import forms
from .models import Client

class ClientForm(forms.ModelForm):

	class Meta:
		model = Client
		fields = ('name','gstatus','appstatus','pstatus','bstatus','astatus','intro','appsub','apppub','applaunch')
