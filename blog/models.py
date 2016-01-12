from django.db import models
from django.contrib import admin

class Blog(models.Model):
	title = models.CharField(max_length=64)
	body = models.TextField()
	time = models.DateTimeField(auto_now=True, null=True)

	def __unicode__(self):
		return unicode('%s' % (self.title))

admin.site.register(Blog)
