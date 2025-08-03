from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class notes(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    date_modified=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.name
    