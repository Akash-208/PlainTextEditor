from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    mail = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date=models.DateField()

# We have define the below function so that we can get the name of the person who is cotacting.
    def __str__(self):
        return self.name
