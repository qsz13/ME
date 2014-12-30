from django.contrib import admin
from story.models import Story, Achievement


class AchievementAdmin(admin.ModelAdmin):

    model = Achievement


class StoryAdmin(admin.ModelAdmin):

    model = Story


admin.site.register(Story, StoryAdmin)
admin.site.register(Achievement, AchievementAdmin)
