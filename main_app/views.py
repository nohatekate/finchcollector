from django.shortcuts import render

# Create your views here.
quarters = [
  {'state': 'Delaware', 'release_date': 'January 4, 1999', 'description': 'Caesar Rodney on horseback Captions: \"The First State\", \"Caesar Rodney\"', 'statehood_date': 'December 7, 1787'},
  {'state': 'Pennsylvania', 'release_date': 'March 8, 1999', 'description': 'Commonwealth statue, state outline, keystone Caption: \"Virtue, Liberty, Independence\"', 'statehood_date': 'December 12, 1787'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def quarters_index(request):
    return render(request, 'quarters/index.html', {
        'quarters': quarters
    })