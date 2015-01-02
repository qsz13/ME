from django.contrib import admin
from story.models import *


class AchievementAdmin(admin.ModelAdmin):

    model = Achievement


class StoryAdmin(admin.ModelAdmin):

    model = Story

class ActivityAdmin(admin.ModelAdmin):

    model = Activity

class TravelAdmin(admin.ModelAdmin):

    model = Travel

class MeaningAdmin(admin.ModelAdmin):

    model = Meaning

class NoteAdmin(admin.ModelAdmin):

    model = Note

admin.site.register(Story, StoryAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Travel, TravelAdmin)
admin.site.register(Meaning, MeaningAdmin)
admin.site.register(Note, NoteAdmin)