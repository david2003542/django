import uuid

from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    gender = models.CharField(
        max_length=100,
        choices=GENDER_CHOICES,
        default='MALE',
    )
    phone = models.CharField(max_length=100)
