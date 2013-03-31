from django.db import models
from django.contrib import admin

class Film(models.Model):
	nowshowing='nowshowing'
	nextchage='nextchange'
	film_status_choices=(
		(nowshowing, 'Now Showing'),
		(nextchage, 'Next Change'),
	)
		
	film_id=models.IntegerField()
	film_name=models.CharField(max_length=100)
	film_image = models.ImageField('Film Image', upload_to='.')
	release_date=models.DateField()
	show_timing=models.TimeField()
	ticket_charge=models.IntegerField()
	film_status=models.CharField(max_length=50, choices=film_status_choices, default=nowshowing)
	hall_id=models.IntegerField()
	description=models.TextField()

	def __unicode__(self):
		return self.film_name

