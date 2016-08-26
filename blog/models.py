from __future__ import unicode_literals
from taggit.managers import TaggableManager
from django.db import models

# Create your models here.

class Post(models.Model) :
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField()
	tags=TaggableManager()	
	
	def __str__(self) :
		return self.title

	



