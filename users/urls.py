from django.urls import path
from users.views.mentors import MentorsView
from users.views.users import UsersView
from users.views.profiles import ProfileView

app_name = "usersapp"

urlpatterns = [
    path('users/', UsersView.as_view(), name='users'),
    path('mentors/', MentorsView.as_view(), name='mentors'),
    path('profiles/', ProfileView.as_view(), name='profiles'),
]