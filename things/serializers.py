from things.models import Thing, Collection, Place, Container
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from django.contrib.auth.models import User, Group

class ThingSerializer(ModelSerializer):
    class Meta:
        model = Thing
        fields = ["id", "name", "description", "location", "owner", "favorite"]

class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "name", "things"]

class ContainerSerializer(ModelSerializer):
    class Meta:
        model = Container
        fields = ["id", "name", "things"]

class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "name", "things", "containers"]

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields= ['username', 'email']
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        