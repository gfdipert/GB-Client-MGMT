from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Client
from .forms import ClientForm

# Create your views here.

def client_list(request):
    """Display list of clients"""
    clients = Client.objects.all().order_by('intro')
    return render(request, 'blog/client_list.html', {'clients':clients})

def client_detail(request, pk):
	"""Display individual client detail page"""
	client = get_object_or_404(Client, pk=pk)
	return render(request, 'blog/client_detail.html', {'client': client})

def client_new(request):
	"""Create new client"""
	if request.method == "POST":
		form = ClientForm(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			client.applaunch = timezone.now()
			client.save()
			return redirect('client_detail', pk=client.pk)
	else:
		form = ClientForm()
	return render(request, 'blog/client_edit.html', {'form':form})

def client_edit(request, pk):
	client = get_object_or_404(Client, pk=pk)
	if request.method == "POST":
		form = ClientForm(request.POST, instance=client)
		if form.is_valid():
			client = form.save(commit=False)
			client.applaunch = timezone.now()
			client.save()
			return redirect('client_detail', pk=client.pk)
	else:
		form = ClientForm(instance=client)
	return render(request, 'blog/client_edit.html', {'form': form})
