from django.shortcuts import render

# Create your views here.
quarters = [
  {'state': 'Delaware', 'release_date': 'January 4, 1999', 'description': 'Caesar Rodney on horseback Captions: \"The First State\", \"Caesar Rodney\"', 'statehood_date': 'December 7, 1787', 'Engraver': 'William Cousins'},
  {'state': 'Pennsylvania', 'release_date': 'March 8, 1999', 'description': 'Commonwealth statue, state outline, keystone Caption: \"Virtue, Liberty, Independence\"', 'statehood_date': 'December 12, 1787', 'Engraver': 'John Mercanti'},
  {'state': 'New Jersey', 'release_date': 'May 17, 1999', 'description': 'Washington Crossing the Delaware, which included George Washington (standing) and James Monroe (holding the flag) Caption: \"Crossroads of the Revolution\"', 'statehood_date': 'December 18, 1787', 'Engraver': 'Alfred Maletsky'},
  {'state': 'Georgia', 'release_date': 'July 19, 1999', 'description': 'Peach, live oak (state tree) sprigs, state outline Banner with text: \"Wisdom, Justice, Moderation\" (the state motto)', 'statehood_date': 'January 2, 1788', 'Engraver': 'T. James Ferrell'},
  {'state': 'Connecticut', 'release_date': 'October 12, 1999', 'description': 'Charter Oak Caption: \"The Charter Oak\"', 'statehood_date': 'January 9, 1788', 'Engraver': 'T. James Ferrell'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def quarters_index(request):
    return render(request, 'quarters/index.html', {
        'quarters': quarters
    })