from django.db import models

# Create your models here.
class ckdModel(models.Model):

    age=models.IntegerField()
    GENDER= [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    sex=models.CharField(max_length=1, choices=GENDER)
    bmi=models.FloatField()
    children=models.IntegerField()
    smoker=models.FloatField()
