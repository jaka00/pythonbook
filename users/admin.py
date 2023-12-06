from django.contrib import admin
from .models.mentors import Mentor
from .models.profiles import Profile
# from users.models.mentors import Mentor


# Register your models here.

admin.site.register(Mentor)
admin.site.register(Profile)