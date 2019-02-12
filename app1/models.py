from django.db import models

# Create your models here.
class Image(models.Model):
	name = models.CharField(max_length = 100)
	picture = models.ImageField(upload_to = 'pictures')

	class Meta:
		db_table = "image"