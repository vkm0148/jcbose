from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	token = models.CharField(max_length=10)

class Post(models.Model):
	post = models.CharField(max_length=500, default="")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	Name = models.CharField(max_length=500, default="")
	Fathers_name = models.CharField(max_length=500, default="")
	Mothers_name = models.CharField(max_length=500, default="")
	Email_id = models.EmailField(blank=True, unique=True)
	Resedential_address=models.CharField(max_length=500, default="")

	def __str__(self):
		return str(self.Email_id)