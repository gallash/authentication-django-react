from django.contrib.auth.models import User, Group
from rest_framework import viewsets  # Creating class-based views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions  # Creating permissions to our views
from .serializers import UserSerializer, GroupSerializer, TestSerializer
from .models import TestModel
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

# No need to use 'render' from 'django.shortcuts' because we are creating 
# class-based views


# Admin ---------------- #
# username: admin
# password: password123
# ---------------------- #

@api_view(['GET'])
# @permission_classes([DjangoModelPermissionsOrAnonReadOnly])
def connection_test(request):  # 'connection-test-function-based'
    class Item():
        # 'item' contains the fields required by the serializer
        def __init__(self, item):
            self.item = item
            
    if request.method == "GET":
        # queryset = TestModel.objects.all()
        item = Item("Hello World!")
        serializer = TestSerializer(item)
        return Response(serializer.data)


# Create your views here.
class ConnectionTest(APIView):  # 'connection-test'
    # Since this is not a "viewset", it'd need some extra 
    # things, namely "get_extra_actions"

    queryset = TestModel.objects.all()  # Mandatory for API enpoints in DRF
    def get(self, request):
        serializer = TestSerializer("Hello World")
        return Response(serializer.data)

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