from django.db import models

class Station(models.Model):
	'''
	Model class for storing info about different weather stations
	'''

	station_name = models.CharField('Station Name', max_length=256, unique=True)
	alias = models.CharField('Station Alias', max_length=256)
	city = models.CharField('Station City', max_length=256)
	country = models.CharField('Station Country', max_length=256, null=True, blank=True)