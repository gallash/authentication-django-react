from django.contrib.auth.models import User, Group
from rest_framework import viewsets  # Creating class-based views
from rest_framework import permissions  # Creating permissions to our views
from .serializers import UserSerializer, GroupSerializer
# No need to use 'render' from 'django.shortcuts' because we are creating 
# class-based views


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    An API endpoint that allows users to be viewed or edited
    """
    # the negative sign indicates descending order
    queryset = User.objects.all().order_by('-date_joined')

    serializer_class = UserSerializer

    # If not authenticated, cannot access it
    permission_classes = [permissions.IsAuthenticated]
    

class GroupViewSet(viewsets.ModelViewSet):
    """
    An API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]