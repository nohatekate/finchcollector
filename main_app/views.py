from django.shortcuts import render
from .models import Quarter
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def quarters_index(request):
    quarters = Quarter.objects.all()
    return render(request, 'quarters/index.html', {
        'quarters': quarters
    })

