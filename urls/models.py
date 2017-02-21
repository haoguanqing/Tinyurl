from django.db import models

class UrlModel(models.Model):
	short_url = models.CharField(max_length=32)
	long_url = models.CharField(max_length=300)

	def __str__(self):
		return self.short_url + ' --> ' + self.long_url
