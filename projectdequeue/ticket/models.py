from django.db import models
from django.contrib import admin

class Ticket(models.Model):
	ticket_id=models.AutoField(primary_key=True)
	film_name=models.CharField(max_length=100)
	end_user=models.CharField(max_length=100)
	purchase_datetime=models.DateTimeField()
	ticket_amount=models.IntegerField()

admin.site.register(Ticket)
