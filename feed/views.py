from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from feed.serializers import UserSerializer, GroupSerializer, WorkSerializer, HolderSerializer
from .models import Work, Holder


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class HolderViewSet(viewsets.ModelViewSet):
    queryset = Holder.objects.all()
    serializer_class = HolderSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]