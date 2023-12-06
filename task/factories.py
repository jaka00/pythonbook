from task.models import factory
from django.contrib.auth.models import User
from users.models.mentors import Mentor
from users.models.profiles import Profile
from task.models.task import *
from django.contrib.auth.hashers import make_password

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f"test_user_{n}")
    password = factory.LazyFunction(lambda: make_password('pi3.1415'))
    is_staff = True
    is_superuser = True

class MentorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mentor
    name = 'test_mentor'
    user = factory.SubFactory(UserFactory)

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
    user = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: f"test_profile {n}")

class TestTaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task
    name = factory.Sequence(lambda n: f"Test task {n}")
    description = "request_post"
    difficulty = 1
    created_by =factory.SubFactory(UserFactory)

class TestAnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Answer
    task = factory.SubFactory(TestTaskFactory)
    profile = factory.SubFactory(ProfileFactory)
    txt = factory.Sequence(lambda n: f"Test answer {n}")