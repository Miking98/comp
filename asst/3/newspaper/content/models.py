from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    text = models.TextField(blank=True)

    def show():
    	return title+": "+subtitle+", By "+contributors+". Published "+pub_date


class Contributor(models.Model):
	first_name = models.CharField(max_length=500)
	last_name = models.CharField(max_length=500)

	def die():
		models.delete()