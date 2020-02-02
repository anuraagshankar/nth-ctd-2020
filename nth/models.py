from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    college = models.TextField(default="N/A")
    mobile_number = models.BigIntegerField(default=0)
    level = models.IntegerField(default=1)
    last_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.user.username