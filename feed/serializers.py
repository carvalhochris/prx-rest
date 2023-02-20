from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework import serializers
from .models import Work, Holder


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class WorkSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    holder = serializers.SerializerMethodField()

    def get_holder(self, obj):
        return obj.holder.all().values_list('name', flat=True)

    class Meta:
        model = Work
        fields = ['xref', 'title', 'holder']

class HolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holder
        fields = ['name', 'email']