from django.contrib import admin
from story.models import *


class AchievementAdmin(admin.ModelAdmin):

    model = Achievement


class StoryAdmin(admin.ModelAdmin):

    model = Story

class ActivityAdmin(admin.ModelAdmin):

    model = Activity



admin.site.register(Story, StoryAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Activity, ActivityAdmin)
