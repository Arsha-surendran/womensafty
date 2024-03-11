from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Uprofile")
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    guardian_name=models.CharField(max_length=200,null=True)
    guardian_phone=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(upload_to="profilepic",null=True,blank=True)

    def str(self):
        return self.user.username

def create_profile(sender,created,instance,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("created")

class Safty(models.Model):
    name=models.CharField(max_length=200)

    def _str_(self):
        return self.name



class Complaint(models.Model):
    complainant = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint #{self.pk}"





post_save.connect(create_profile,sender=User)