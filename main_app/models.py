from django.db import models

# Create your models here.
class Quarter(models.Model):
    state_name = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    statehood_date = models.CharField(max_length=50)
    engraver = models.CharField(max_length=50)
    

    def __str__(self):
        return self.state_name