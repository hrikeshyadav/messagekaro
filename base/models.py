from django.db import models

# Create your models here.
class Message(models.Model):
   name = models.CharField( max_length=30 )
   email = models.EmailField( max_length=100 )
   mob = models.CharField( max_length=10)
   msg = models.CharField( max_length=300 )