from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone
from model_utils.managers import InheritanceManager


class StoryManager(models.Manager):
    def create_achievement(self,author ,title, content, mood, image=None):
        achievement = self.create(author=author, title=title, content=content,mood=mood, image=image)
        return achievement


class Story(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now())
    content = models.TextField()
    mood = models.TextField(blank=True)
    objects = InheritanceManager()
    author = models.ForeignKey(User, blank=True)
    def __unicode__(self):
        return "Achievement "+self.title


class Achievement(Story):
    image = models.ImageField(blank=True)
    objects = StoryManager()


class Travel(Story):
    together_with = models.TextField()
    place = models.TextField()
    objects = StoryManager()

class Milestone(Story):
    wishes = models.TextField()
    objects = StoryManager()

class Activity(Story):
    together_with = models.TextField()
    place = models.TextField()
    objects = StoryManager()

class ImageSet(models.Model):
    #Story = models.ForeignKey(Story, related_name='images')
    objects = StoryManager()
    image = models.ImageField()


class VideoSet(models.Model):
    #Story = models.ForeignKey(Story, related_name='video')
    video = models.FileField()
    objects = StoryManager()


# def get_all_story_by_user(user):
#     a = Achievement.objects.filter(author=user).order_by('-time')
#
#     return a




