from django.contrib.auth.models import User
from Depreciation.models import Assets, Depreciation
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('Name', 'Price', 'SerialNumber', 'Assignee', 'DOA', 'DepClass')


class DepreciationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Depreciation
        fields = ('Class', 'Rate')