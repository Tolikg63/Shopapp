from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GroupSerializer


@api_view()
def hello_world_view(request):
    return Response({"message": "Hi I'm here"})


@api_view()
def group_view(request):
    groups = Group.objects.all()
    data = [group.name for group in groups]
    return Response({"group": data})


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        data = [user.username for user in users]
        return Response({"User": data})
    

class GroupListView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serialized = GroupSerializer(groups, many=True)
        return Response({'message': serialized.data})