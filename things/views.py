from django.shortcuts import render, get_object_or_404
from things.models import Thing, Collection, Container, Place
from django.contrib.auth.models import User, Group
from things.serializers import RegisterUserSerializer, ThingSerializer, CollectionSerializer, UserSerializer, GroupSerializer, ContainerSerializer, PlaceSerializer
from rest_framework.viewsets import ModelViewSet, ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters, generics, permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated, AllowAny, DjangoModelPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class ThingEditPermission(BasePermission):
    messege = 'Only the owner may edit this thing.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user

class ThingViews(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ThingSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Thing, slug=item)

    def get_queryset(self):
            return Thing.objects.all()

class ThingListDetailFilter(generics.ListAPIView):

    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

class ThingSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset =Thing.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

class CollectionViews(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [AllowAny]

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Collection, slug=item)

    def get_queryset(self):
            return Collection.objects.all()

class ContainerViews(ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    permission_classes = [AllowAny]

class PlaceViews(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [AllowAny]

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

class BlacklistTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GroupViews(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

#CRUD Functions

class CreateThing(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class EditThingDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class EditThing(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class DeleteThing(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer