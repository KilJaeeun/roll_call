from django.db import models


# Create your models here.
from roll_call import tests


class FloorManager(models.Model):
    floor_num = models.IntegerField(null=False)





class Student(models.Model):
    ssn = models.CharField(max_length=7, default='교환학생')
    name = models.CharField(max_length=30, default='unknown')
    phone = models.CharField(max_length=30, default='unknown')
    mother_phone = models.CharField(max_length=30, default='unknown')
    status = models.CharField(max_length=10, choices=tests.status,default='미입사')
    room_num = models.CharField(max_length=10)
    floor_num = models.ForeignKey(FloorManager, on_delete=models.CASCADE)