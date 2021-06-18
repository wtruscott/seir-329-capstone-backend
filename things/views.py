from django.shortcuts import render
from things.models import Thing, Collection
from django.contrib.auth.models import User, Group
from things.serializers import RegisterUserSerializer, ThingSerializer, CollectionSerializer, UserSerializer, GroupSerializer
from rest_framework.viewsets import ModelViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class ThingViews(ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

class CollectionViews(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

class UserViews(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserCreate(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupViews(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)