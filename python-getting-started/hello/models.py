from django.db import models

# Create your models here.

class Bid(models.Model):
	event = models.CharField(max_length=30)
	team = models.CharField(max_length=30)
	teamt = models.CharField(max_length=30)
	date = models.DateField(auto_now_add=True)
	mini = models.CharField(max_length=30)
	maxi = models.CharField(max_length=30)
	bwin = models.CharField(max_length=300)
	bet = models.CharField(max_length=300)

	def __str__(self):
		return self.event