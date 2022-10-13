from django.db import models

# Create your models here.

class Art(models.Model):

    title=models.CharField(max_length=10)
    content=models.TextField()
    writer=models.IntegerField()
    
    score=models.IntegerField(default=0)
    count=models.IntegerField(default=0)
