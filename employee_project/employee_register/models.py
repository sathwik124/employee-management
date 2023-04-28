import os
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<username>/<filename>
    return os.path.join(instance.user.username, filename)

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    
class Employee(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    manager = models.ForeignKey('self',on_delete=models.CASCADE,default=2)
    profile_pic = models.ImageField(upload_to = user_directory_path,default = "default.png",null=True,blank=True)
    def __str__(self):
        return self.fullname