from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class PoliceProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Pprofile")
    name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(upload_to="profilepic",null=True,blank=True)

    def str(self):
        return self.user.username

def create_profile(sender,created,instance,**kwargs):
    if created:
        PoliceProfile.objects.create(user=instance)
        print("created")