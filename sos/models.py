from datetime import datetime
from django.urls import reverse
from django.db import models

# Create your models here.


class Sos(models.Model):
    class Meta:
        ordering= ["-id"]
    date= models.DateField(max_length=30,help_text="Date",default=datetime.now)
    id= models.CharField(max_length=30,primary_key='True',help_text="Id")
    uid= models.CharField(max_length=30,help_text="Uid")
    name= models.CharField(max_length=50,help_text="Name")
    level=models.IntegerField(help_text="Enter Level")
    content=models.CharField(max_length=100,help_text="Enter Content")
    media= models.CharField(max_length=20,help_text="Media")

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('model-detail-view', args=[str(self.id)])