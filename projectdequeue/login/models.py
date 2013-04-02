from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class EndUser(models.Model):
	user=models.ForeignKey(User)
	credits=models.IntegerField(default=0)
	
admin.site.register(EndUser)
