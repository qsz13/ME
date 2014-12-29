from django.contrib.auth.models import User
from django.db.models import OneToOneField, Model, CharField, ImageField
from django.db.models.signals import post_save


class Profile(Model):
    user = OneToOneField(User, related_name='profile')
    phone = CharField(max_length=15, blank=True)
    avatar = ImageField(upload_to='avatar', default="/media/avatar/default", blank=True)
    def __str__(self):
        return self.user.username+" profile"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)