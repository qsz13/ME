from __future__ import absolute_import

from django.contrib import admin

from .models import Friend, FriendshipRequest



class FriendAdmin(admin.ModelAdmin):
    model = Friend
    raw_id_fields = ('to_user', 'from_user')


class FriendshipRequestAdmin(admin.ModelAdmin):
    model = FriendshipRequest
    raw_id_fields = ('from_user', 'to_user')



admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendshipRequest, FriendshipRequestAdmin)
