from django.db import models

class Video(models.Model):
	video_title = models.CharField(max_length=250)
	videos = models.FileField(upload_to='videos/' , null=True)
