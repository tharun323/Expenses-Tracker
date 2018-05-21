from django.db import models

class Item(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    price=models.IntegerField(null= True,blank=True)
    image=models.FileField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


