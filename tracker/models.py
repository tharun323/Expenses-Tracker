from django.db import models
from django.utils import timezone
import datetime
class Item(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.IntegerField(null= True)
    image=models.FileField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

