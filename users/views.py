from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from rest_framework.views import APIView, View
from rest_framework.response import Response

from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, RegisterSerializer, ProfileSerializer
from .models import CustomUser, Profile


class HelloView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


# class ProfileViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated] 


class UpdateProfileView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        user = self.request.user
        serializer = self.serializer_class(user.profile, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
