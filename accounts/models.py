from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.FileField(upload_to=profile_picture_upload_to, blank=True, null=True)
    realtor = models.CharField(max_length=50)
    agent_id = models.CharField(max_length=50)
    plan = models.IntegerField(default=0)
