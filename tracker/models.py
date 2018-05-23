from django.db import models
from django.utils import timezone
import datetime
class Item(models.Model):
    name=models.CharField(max_length=200,null=True)  #Item name
    price=models.IntegerField(null= True)            #price name
    image=models.FileField(blank=True,null=True)     # image field
    created_at = models.DateTimeField(auto_now_add=True) #created time

    def __str__(self):    #returns name of item on reference
        return self.name

