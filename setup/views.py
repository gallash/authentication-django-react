from django.contrib.auth.models import User, Group
from rest_framework import viewsets  # Creating class-based views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions  # Creating permissions to our views
from .serializers import UserSerializer, GroupSerializer
from .models import TestModel
from rest_framework.decorators import action

# No need to use 'render' from 'django.shortcuts' because we are creating 
# class-based views


# Admin:
# username: admin
# password: password123


# Create your views here.
class ConnectionTest(APIView):
    # Since this is not a "viewset", it'd need some extra 
    # things, namely "get_extra_actions"

    queryset = TestModel.objects.all()  # Mandatory for API enpoints in DRF
    def get(self, request):
        return Response("Hello World!")  # No serialization required?

    # The following things are not properly implemented and is not operational
    # but is kept for later studies
    # @action(detail=True, methods=['get'], url_path='new_action')
    # def new_action(self, request):
    #     return Response("A new action")
    
    # @classmethod
    # def get_extra_actions(cls):
    #     return {
    #         'new_action': cls.new_action
    #     }


# Unused classes. They stay for reference
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