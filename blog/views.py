from django.shortcuts import render
from .models import Post
from .models import Client
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
    clients = Client.objects.filter(intro__lte=timezone.now()).order_by('intro')
    return render(request, 'blog/post_list.html', {'clients':clients})

def client_detail(request, cl):
    post = get_object_or_404(Post, cl=cl)
    return render(request, 'blog/client_detail.html', {'client': client})
