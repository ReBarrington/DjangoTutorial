from django.db.models.signals import post_save
# gets fired after object is saved/ when user is created
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


