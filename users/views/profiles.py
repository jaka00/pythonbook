from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import ProfileSerializer
from users.models.profiles import Profile



class ProfileView(APIView):
    def get(self, request, *args, **kwargs):
        profile_list = Profile.objects.all()
        profile_serializer = ProfileSerializer(profile_list, many=True)
        return Response(profile_serializer.data)