from django.db import models

# Create your models here.

class DoctorModel(models.Model):
    ROLE_CHOICES=(
        ('doctor','doctor'),
        ('staff','staff'),
        ('nurse','nurse'),
        ('worker','worker')
    )
    name=models.CharField(max_length=70,null=True,blank=True)
    unique_id=models.CharField(null=True,blank=True)
    field=models.CharField(null=True,blank=True)
    role=models.CharField(choices=ROLE_CHOICES,null=True,blank=True,max_length=10)

    def __str__(self):
        return self.name