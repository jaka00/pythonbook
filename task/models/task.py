from django.db import models
from users.models.mentors import Mentor
from users.models.profiles import Profile
from django.contrib.auth.models import User

difficulty_choices = (
    (1, "Очень лёгкий"),
    (2, "Лёгкий"),
    (3, "Средний"),
    (4, "Сложный"),
    (5, "Очень сложный"),
)

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.IntegerField(choices=difficulty_choices)
    created_by = models.ForeignKey(to=User, on_delete=models.PROTECT)
    # created_by = models.OneToOneField(Mentor, on_delete=models.CASCADE)
    # upload_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["difficulty"]

#decision
class Answer(models.Model):
    task =  models.ForeignKey(Task,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    txt = models.TextField()
    correctly = models.BooleanField(default=False)

    created_by = models.DateTimeField(auto_now_add=True)
    update_by = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_by"]