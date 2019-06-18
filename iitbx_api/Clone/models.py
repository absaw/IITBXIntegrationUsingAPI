from django.db import models

# Create your models here.
class repoclone(models.Model):
	Course = models.TextField()
	Directory = models.TextField()
	Status = models.TextField(blank = True)

	def __str__(self):
		return self.url
