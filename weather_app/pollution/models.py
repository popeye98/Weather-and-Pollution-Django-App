from django.db import models
from datetime import datetime
# Create your models here.
class Pollution(models.Model):
    name=models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    

    def __str__(self):
        return self.name