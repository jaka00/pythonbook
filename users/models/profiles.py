from django.db import models
from django.contrib.auth.models import User
# from task.models.task import Answer

class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.PROTECT
    )
    name = models.CharField(
        max_length=60
    )
    description = models.TextField(null=True,blank=True)
    # answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)

    created_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name