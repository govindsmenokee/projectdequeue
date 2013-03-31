from django.db import models

class Hall(models.Model):
	hall_id=models.IntegerField()
	total_seats=models.IntegerField()
	total_seats_allocated=models.IntegerField()

def __unicode__(self):
		return self.hall_id


