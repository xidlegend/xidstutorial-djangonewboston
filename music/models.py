from django.db import models
from django.urls import reverse


# Models created here will automaticaly e added to the database
class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=250)
	genre = models.CharField(max_length=100)
	album_logo = models.FileField()

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk': self.pk})

	#This is to Print the album title and artist name when requested
	#Album.objects.all() from the django sell
	def __str__(self):
		return self.album_title + ' - ' + self.artist


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=100)
	is_favorite = models.BooleanField(default=False)
	
	def __str__(self):
		return self.song_title


