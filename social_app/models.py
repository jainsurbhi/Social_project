from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.signals import pre_save 
from django.dispatch import receiver

@receiver(pre_save, sender=User)
def update_username_from_email(sender, instance, **kwargs):
    instance.username = instance.email