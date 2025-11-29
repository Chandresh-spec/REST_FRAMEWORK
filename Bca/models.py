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







class Info(models.Model):
    CURRENT_YEAR=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
    )
    name=models.CharField(max_length=100,null=True,blank=True)
    rno=models.CharField(max_length=10,null=True,blank=True)
    year=models.CharField(choices=CURRENT_YEAR,null=True,blank=True)


    def __str__(self):
        return self.name



class Teacher(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    branch=models.CharField(max_length=100,null=True,blank=True)
    experience=models.IntegerField()