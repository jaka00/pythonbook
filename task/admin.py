from django.contrib import admin
from .models.task import *


admin.site.register(Task)
admin.site.register(Answer)