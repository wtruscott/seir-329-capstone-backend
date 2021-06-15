from things.models import Thing, Collection
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth.models import User, Group

class ThingSerializer(ModelSerializer):
    class Meta:
        model = Thing
        fields = ["id", "name", "description", "location", "favorite"]

class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "name", "things"]

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        