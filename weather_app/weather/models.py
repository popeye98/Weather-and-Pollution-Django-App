from django.db import models
from datetime import datetime
# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    

    def __str__(self):
        return self.name
    