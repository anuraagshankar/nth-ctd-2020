from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    college = models.TextField(default="N/A")
    mobile_number = models.BigIntegerField(default=0)
    level = models.IntegerField(default=1, db_index=True)
    last_time = models.DateTimeField(auto_now=True)
    reg_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
