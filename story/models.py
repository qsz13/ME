from django.db import models

# Create your models here.

class Story(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100)
    time = models.DateTimeField()
    content = models.TextField()
    mood = models.TextField()

class Achievement(Story):
    together_with = models.TextField()


class Travel(Story):
    together_with = models.TextField()
    place = models.TextField()

class Milestone(Story):
    wishes = models.TextField()


class Activity(Story):
    together_with = models.TextField()
    place = models.TextField()


class ImageSet(models.Model):
    Story = models.ForeignKey(Story, related_name='images')
    image = models.ImageField()


class VideoSet(models.Model):
    Story = models.ForeignKey(Story, related_name='video')
    video = models.FileField()
