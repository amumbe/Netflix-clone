from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.

AGE_LIMIT = (
    ("All", "All"),
    ("Kids", "Kids"),
)

MOVIE_CHOICES =(
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)


class CustomUser(AbstractUser):
    profiles = models.models.ManyToManyField("Profile", blank=True)


class Profile(models.Model):
    name = models.CharField(max_length=1000)
    age_limit = models.CharField(choices=AGE_LIMIT, max_length=10)
    uuid = models.UUIDField(default=uuid.uuid4)


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    uuid = models.UUIDField(default= uuid.uuid4)
    type = models.CharField(choices = MOVIE_CHOICES, max_length = 100 )

