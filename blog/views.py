from django.shortcuts import render
from .models import Post
from .models import Client
from django.utils import timezone

# Create your views here.

def post_list(request):
    clients = Client.objects.filter(applaunch__lte=timezone.now()).order_by('applaunch')
    return render(request, 'blog/post_list.html', {'clients':clients})
