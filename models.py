from django.db import models

# Create your models here.
class ckdModel(models.Model):

    age=models.FloatField()
    GENDER= [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    sex=models.CharField(max_length=1, choices=GENDER)
    bmi=models.FloatField()
    children=models.FloatField()
    smoker=models.FloatField()
