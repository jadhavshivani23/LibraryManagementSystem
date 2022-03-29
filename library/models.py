from django.db import models

# Create your models here.
class Books(models.Model):
    Book_ID = models.AutoField(primary_key=True)
    Book_Name = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Book_Price = models.FloatField()
