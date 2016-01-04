from django.shortcuts import render
from .models import Post
from .models import Client
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import ClientForm

# Create your views here.

def client_list(request):
    clients = Client.objects.filter(intro__lte=timezone.now()).order_by('intro')
    return render(request, 'blog/client_list.html', {'clients':clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'blog/client_detail.html', {'client': client})

def client_new(request):
	form = ClientForm()
	return render(request, 'blog/client_edit.html', {'form':form})
