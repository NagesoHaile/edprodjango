from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email= models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)


    def __str__(self):
        return self.first_name +" "+ self.middle_name