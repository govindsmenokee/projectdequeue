from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
class EndUser(models.Model):
	user=models.ForeignKey(User)
	credits=models.IntegerField(default=0)
        headshot = models.ImageField(upload_to='img', blank=True)
        text = models.TextField('Desc', max_length=500, blank=True)
		
admin.site.register(EndUser)
