from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    
class Employee(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True,blank=True)
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    manager = models.ForeignKey('self',on_delete=models.CASCADE,default=2)

    def __str__(self):
        return self.fullname