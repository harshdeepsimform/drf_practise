from django.shortcuts import render



from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .models import Station, Slot
# from users.serializers import UserSerializer, GroupSerializer
from .serializers import StationSerializer


class ReadOnly(BasePermission):
    '''
    CUSTOM PERMISSION
    '''
    
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Station.objects.all().order_by('-created_at')
    serializer_class = StationSerializer
    permission_classes = [IsAuthenticated|ReadOnly]



class SlotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Slot.objects.all().order_by('-created_at')
    serializer_class = SlotSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]