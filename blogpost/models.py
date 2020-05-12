
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title 

class Place(models.Model):
    place = models.CharField(max_length=200)
    review= models.TextField()
    score= models.IntegerField() 
    # checklist는 어떤 타입이라고 해야 하징..

class Beauty(models.Model):
    b_diary = models.TextField()
    cosmetics= models.TextField()
    sleep =models.IntegerField()
