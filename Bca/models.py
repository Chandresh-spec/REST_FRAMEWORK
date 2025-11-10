from django.db import models

# Create your models here.



class Color(models.Model):
    color=models.CharField(max_length=10)


    def __str__(self):
        return self.color.upper()
    




class Student(models.Model):
    grade=models.CharField(max_length=2)
    name=models.CharField(max_length=100)
    age=models.IntegerField()


    def __str__(self):
        return self.name






