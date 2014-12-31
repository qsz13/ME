from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone
from model_utils.managers import InheritanceManager


class AchievementManager(models.Manager):
    def create_achievement(self,author ,title, content, mood, image=None):
        achievement = self.create(author=author, title=title, content=content,mood=mood, image=image)
        return achievement

class ActivityManeger(models.Manager):
    def create_activity(self, author, title, content, mood,  together_with, place, image=None):
        activity = self.create(author=author, title=title, content=content,
                               mood=mood, together_with=together_with, place=place, image=image)
        return activity


class GrowthManager(models.Manager):
    def create_growth(self, author, title, content, mood, age, weight, height, image = None):
        growth = self.create(author=author, title=title, content=content, mood=mood, age=age,
                             weight=weight, height=height, image=image)
        return growth


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
    objects = AchievementManager()


class Activity(Story):
    together_with = models.TextField()
    place = models.TextField()
    objects = ActivityManeger()
    image = models.ImageField(blank=True)


class Growth(Story):
    wishes = models.TextField()
    age = models.CharField(max_length=16)
    weight = models.CharField(max_length=16)
    height = models.CharField(max_length=16)
    objects = GrowthManager()


class Travel(Story):
    together_with = models.TextField()
    place = models.TextField()
    #objects = StoryManager()


class ImageSet(models.Model):
    #Story = models.ForeignKey(Story, related_name='images')
   # objects = StoryManager()
    image = models.ImageField()


class VideoSet(models.Model):
    #Story = models.ForeignKey(Story, related_name='video')
    video = models.FileField()
   # objects = StoryManager()


# def get_all_story_by_user(user):
#     a = Achievement.objects.filter(author=user).order_by('-time')
#
#     return a




