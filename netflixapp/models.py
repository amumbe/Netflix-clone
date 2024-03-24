from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.

AGE_LIMIT =(
    ('All', 'All'),
    ('Kids', 'Kids'),
)

class CustomUser(AbstractUser):
    profiles = models.models.ManyToManyField("Profile", blank = True)


class Profile(models.Model):
    name = models.CharField(max_length = 1000)
    age_limit =