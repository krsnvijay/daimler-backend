from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from rest_framework.authtoken.models import Token

from critical_list.models import Part


class User(AbstractUser):
    phone = models.CharField(max_length=10, help_text="Enter Phone Number")
    starred_parts = models.ManyToManyField(Part, help_text="Parts Starred by the user", related_name='user_starred',
                                           blank=True)
    REQUIRED_FIELDS = 'phone', 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('user-detail', args=[str(self.id)])


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
