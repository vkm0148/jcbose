from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Post(models.Model):
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	Name = models.CharField(max_length=500)
	Fathers_name = models.CharField(max_length=500)
	Mothers_name = models.CharField(max_length=500)
	Mobile_no = models.IntegerField()
	Email_id = models.EmailField()
	Resedential_adress=models.CharField(max_length=500)