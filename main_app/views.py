from django.shortcuts import render

# Create your views here.
finches = [
  {'name': 'Dan', 'breed': 'finch', 'description': 'loud', 'age': 3},
  {'name': 'Kate', 'breed': 'finch', 'description': 'quiet', 'age': 2},
]

def home(request):
    return render(request, 'home.html')